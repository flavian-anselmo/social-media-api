// serverfarm 
param location_one string   = 'eastus'
param operatingSys string = 'linux'
param skuName string  = 'B1'
param  socialMediaServicePlanName string = 'social-media-linux-service-plan'


// site 
param socialmediaPlanName string = 'social-media-linux-service-plan'
param siteName string = 'social-media-api'
param linuxFxVersion string  = 'PYTHON|3.10'
param ALGORITHM string = 'HS256'
param DATABASE_HOST string = 'socialmedia-sandbox-server.postgres.database.azure.com'
param DATABASE_NAME string = 'social-media-api-db'
@secure()
param DATABASE_PASSWORD string 
param DATABASE_PORT string = '8000'
param DATABASE_USERNAME string = 'anselmo@socialmedia-sandbox-server'

param SECRET_KEY string = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

// server 
param location_two string = 'westus3'
param serverName string = 'socialmedia-sandbox-server'
@secure()
param administratorLogin string 
@secure()
param administratorLoginPassword string 


module serverFarm '../../Microsoft.Web/serverfarms.bicep'={
  name:'servicePlan'
  params:{
    location:location_one
    operatingSys:operatingSys
    skuName:skuName
    socialMediaServicePlanName: socialMediaServicePlanName
  }
}

module site '../../Microsoft.Web/sites.bicep'={
  dependsOn:[
    serverFarm
  ]
  name:'appService'
  params: {
    ALGORITHM:ALGORITHM
    DATABASE_HOST:DATABASE_HOST
    DATABASE_NAME:DATABASE_NAME
    DATABASE_PASSWORD:DATABASE_PASSWORD
    DATABASE_PORT:DATABASE_PORT
    DATABASE_USERNAME:DATABASE_USERNAME
    linuxFxVersion:linuxFxVersion
    location:location_one
    SECRET_KEY:SECRET_KEY
    siteName:siteName
    socialmediaPlanName:socialmediaPlanName
  }
}


module postgreSQLServer '../../Microsoft.DBforPostgreSQL/servers.bicep'={
  dependsOn:[
    serverFarm
    site
  ]
  name:'postgreSQLSingleServer'
  params:{
    administratorLogin:administratorLogin
    administratorLoginPassword:administratorLoginPassword
    location:location_two
    serverName:serverName
  }
}

module firewallRules '../../Microsoft.DBforPostgreSQL/servers/firewall_rules.bicep' ={
  dependsOn:[
    postgreSQLServer
    site
    serverFarm
  ]
  name:'firewallRules'
  params:{
    serverName:serverName
  }
}
