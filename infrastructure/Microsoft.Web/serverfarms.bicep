param location string   = 'eastus'
param operatingSys string = 'linux'
param skuName string  = 'F1'
param  socialMediaServicePlanName string = 'social-media-linux-service-plan'

@description('social-media-api app service plan')
resource appServicePlan 'Microsoft.Web/serverfarms@2022-03-01'={
  location:location
  name:socialMediaServicePlanName
  kind:operatingSys
  properties:{
    reserved:true
    zoneRedundant:false
  }
  sku:{
    name:skuName
  }
}

