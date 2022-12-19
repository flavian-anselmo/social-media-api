param location string   
param operatingSys string 
param skuName string  
param  socialMediaServicePlanName string 

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

