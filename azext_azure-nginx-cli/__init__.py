from knack.help_files import helps
from azure.cli.core import AzCommandsLoader
import requests


def deploy_nginx(name, node_sku, node_count, resource_group, location, custom_subnet_id="", server_address="http://localhost:8080"):
    content = {"name": name, "nodeSku": node_sku, "nodeCount": int(
        node_count), "resourceGroup": resource_group, "location": location, "customSubnetID": custom_subnet_id}

    print("Deploying nginx cluster...")
    r = requests.post(server_address + "/nginx", json=content)
    code = r.status_code

    if code is 200:
        return r.json()
    else:
        return r.text


class AzureNginxCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_azure-nginx-cli#{}')
        super(AzureNginxCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=custom_type)

    def load_command_table(self, args):
        with self.command_group('nginx') as g:
            g.custom_command('deploy', 'deploy_nginx')
        return self.command_table

    def load_arguments(self, _):
        pass


COMMAND_LOADER_CLS = AzureNginxCommandsLoader
