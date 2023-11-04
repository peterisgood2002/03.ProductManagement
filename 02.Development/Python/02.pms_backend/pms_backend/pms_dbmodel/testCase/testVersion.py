from .base_test import PMSDbTest
from .data import TestData, CheckData
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
        r = VersionOperation.getVersions(TestData.area, TestData.operator1)
        assert 0 == len(r)

        [version, succeed] = VersionOperation.addVersion(
            TestData.area,
            TestData.operator1,
            TestData.version19,
        )
        CheckData.checkVersion(version, TestData.operator1, TestData.version19)
        assert succeed == True
        [version, succeed] = VersionOperation.addVersion(
            TestData.area,
            TestData.operator1,
            TestData.version19,
        )
        CheckData.checkVersion(version, TestData.operator1, TestData.version19)
        assert succeed == False
        [version, succeed] = VersionOperation.addVersion(
            TestData.area,
            TestData.operator1,
            TestData.version22,
        )
        CheckData.checkVersion(version, TestData.operator1, TestData.version22)
        assert succeed == True

        r = VersionOperation.getVersions(TestData.area, TestData.operator1)
        assert 2 == len(r)
        assert TestData.version19 in r
        assert TestData.version22 in r

        r = VersionOperation.getVersion(TestData.operator1, TestData.version19)
        CheckData.checkVersion(r, TestData.operator1, TestData.version19)
