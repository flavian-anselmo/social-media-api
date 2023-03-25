// serverfarm 
param location_one string   
param operatingSys string 
param skuName string  
param  socialMediaServicePlanName string 


// site 
param socialmediaPlanName string 
param siteName string 
param linuxFxVersion string  
param ALGORITHM string 
param DATABASE_HOST string 
param DATABASE_NAME string 
@secure()
param DATABASE_PASSWORD string 
param DATABASE_PORT string 
param DATABASE_USERNAME string 

param SECRET_KEY string

// server 
param location_two string 
param serverName string 
@secure()
param administratorLogin string 
@secure()
param administratorLoginPassword string 


module serverFarm '../../../../Microsoft.Web/serverfarms.bicep'={
  name:'servicePlan'
  params:{
    location:location_one
    operatingSys:operatingSys
    skuName:skuName
    socialMediaServicePlanName: socialMediaServicePlanName
  }
}

module site '../../../../Microsoft.Web/sites.bicep'={
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


module postgreSQLServer '../../../../Microsoft.DBforPostgreSQL/servers.bicep'={
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

module firewallRules '../../../../Microsoft.DBforPostgreSQL/servers/firewall_rules.bicep' ={
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
