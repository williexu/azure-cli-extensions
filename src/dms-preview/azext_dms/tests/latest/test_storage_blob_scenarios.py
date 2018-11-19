# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer,
                               JMESPathCheck, api_version_constraint)



class ExampleTest(ScenarioTest):
    @ResourceGroupPreparer(location='westus2')
    def test_do_something(self, resource_group):
        self.cmd('az group list')

if __name__ == '__main__':
    unittest.main()
