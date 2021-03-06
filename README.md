# Azure-Nginx Extension for Azure CLI 2.0

![Python](https://img.shields.io/pypi/pyversions/azure-cli.svg?maxAge=2592000)

This Azure CLI 2.0 extension allows you to provision self reliant, PaaS-like nginx clusters on Azure.

## Installation

The extension is designed to be plug-and-play with Azure CLI. **Even** if you have Azure CLI installed make sure it is up to date.

### Step 0: Install/Update Azure CLI

At a minimum your CLI core version must be `2.0.24` or above. Use `az --version` to validate. This version supports `az extension` commands and introduces the `knack` command framework.

Follow the installation instructions on [GitHub](https://github.com/Azure/azure-cli) or [Microsoft Docs](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) to setup Azure CLI in your environment.

### Step 1: Install the extension

Now that you have a compatible Azure CLI installed you can add the azure-nginx extension.
When you install an extension, any additional Python dependencies required are automatically downloaded and installed.

There are multiple options for installation. After installing the extension, you can use `az extension list` to validate the currently installed extensions or `az extension show --name azure-nginx-cli` to see details about the azure-nginx extension.

Install version 0.0.1:

`az extension add --source 'https://github.com/azure-nginx/azure-nginx-cli/raw/master/dist/azure_nginx_cli-0.0.1-py2.py3-none-any.whl'`

## Command-Line Usage

```bash
Command
    az nginx deploy

Arguments
    --location -l    [Required]: Location. You can configure the default location using az
                                 configure --defaults location=<location>.
    --name           [Required]
    --node-count     [Required]
    --node-sku       [Required]
    --resource-group [Required]
    --custom-subnet-id
    --server-address           : Default: http://localhost:8080.

Global Arguments
    --debug                    : Increase logging verbosity to show all debug logs.
    --help -h                  : Show this help message and exit.
    --output -o                : Output format.  Allowed values: json, jsonc, table, tsv.  Default:
                                 json.
    --query                    : JMESPath query string. See http://jmespath.org/ for more
                                 information and examples.
    --verbose                  : Increase logging verbosity. Use --debug for full debug logs.
```

## Usage Examples

The azure-nginx CLI needs to interact with the Azure Nginx Service Provisioner.
Unless specified, the CLI will assume it is running on localhost:8080.

### deploy an nginx cluster of 2 nodes in eastus

`az nginx deploy --name "nginxclusterdemo" --resource-group "nginx-rg" --node-count 2 --node-sku "Standard_D1_V2" --location "eastus"`

### deploy in a custom vnet

`az nginx deploy --custom-subnet-id "<id-of-custom-subnet>" --name "nginxclusterdemo" --resource-group "nginx-rg" --node-count 2 --node-sku "Standard_D1_V2" --location "eastus"`

### deploy with a remote service provisioner

`az nginx deploy --server-address "<ip-or-fqdn-of-service-provisioner>" --name "nginxclusterdemo" --resource-group "nginx-rg" --node-count 2 --node-sku "Standard_D1_V2" --location "eastus"`


