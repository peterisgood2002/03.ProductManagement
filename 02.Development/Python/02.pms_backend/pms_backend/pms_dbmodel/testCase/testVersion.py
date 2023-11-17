from pms_dbmodel.testoperatordata import TestOperatiorData, CheckOperatorData
from .base_test import PMSDbTest
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.operator_operation.version_operation import VersionOperation


class VersionOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EComplianceVersion,
        )

    def testGetVersions(self):
        r = VersionOperation.getVersions(
            TestOperatiorData.area, TestOperatiorData.operator1
        )
        assert 0 == len(r)

        [version, succeed] = VersionOperation.addVersion(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
        )
        CheckOperatorData.checkVersion(
            version, TestOperatiorData.operator1, TestOperatiorData.version19
        )
        assert succeed == True
        [version, succeed] = VersionOperation.addVersion(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
        )
        CheckOperatorData.checkVersion(
            version, TestOperatiorData.operator1, TestOperatiorData.version19
        )
        assert succeed == False
        [version, succeed] = VersionOperation.addVersion(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version22,
        )
        CheckOperatorData.checkVersion(
            version, TestOperatiorData.operator1, TestOperatiorData.version22
        )
        assert succeed == True

        r = VersionOperation.getVersions(
            TestOperatiorData.area, TestOperatiorData.operator1
        )
        assert 2 == len(r)
        assert TestOperatiorData.version19 in r
        assert TestOperatiorData.version22 in r

        r = VersionOperation.getVersion(
            TestOperatiorData.operator1, TestOperatiorData.version19
        )
        CheckOperatorData.checkVersion(
            r, TestOperatiorData.operator1, TestOperatiorData.version19
        )
