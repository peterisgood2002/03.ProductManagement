from pms_dbmodel.common import setDateAndSave, LOGTIME, logInfo
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.operator_operation import logger
from .operator_operation import OperatorOperation


class VersionOperation:
    @classmethod
    def _addVersion(cls, area, operator, version):
        o = OperatorOperation.addOperator(area, operator)

        result = EComplianceVersion.objects.get_or_create(
            operator=o, version_no=version
        )
        setDateAndSave(result)

        return result

    @classmethod
    def addVersion(cls, area, operator, version):
        v = cls._addVersion(area, operator, version)

        logInfo(
            logger,
            LOGTIME.END,
            cls.addVersion.__name__,
            "AREA = %s, Operator = %s, Version = %s, Insert/Update(True/False) = %s",
            area,
            operator,
            version,
            v[1],
        )

        return v

    @classmethod
    def getVersions(cls, area, operator):
        # 1. check whether this operator is the first one
        o = OperatorOperation.getOperator(operator)
        # 2. get the versions for this operator
        versions = EComplianceVersion.objects.filter(operator=o)

        r = []
        for v in versions:
            r.append(v.version_no)

        return r

    @classmethod
    def _getVersion(cls, area, operator, version):
        logger.info(
            "[getVersion][BEGIN] AREA = %s, Operator = %s, Version = %s",
            area,
            operator,
            version,
        )

        v = cls._addVersion(area, operator, version)

        return v[0]

    @classmethod
    def getVersion(cls, operator, version):
        logger.info(
            "[getVersion][BEGIN] Operator = %s, Version = %s", operator, version
        )
        version = EComplianceVersion.objects.filter(
            operator__name=operator, version_no=version
        )
        if len(version) == 0:
            return None

        return version[0]

    @classmethod
    def getOrAddVersion(cls, area, operator, version_no):
        version = VersionOperation.getVersion(operator, version_no)
        if version == None:
            [version, succeed] = VersionOperation.addVersion(area, operator, version_no)
        return version
