param location string = 'westus3'
param serverName string = 'socialmedia-sandbox-server.postgres.database.azure.com'

@secure()
param administratorLogin string 

@secure()
param administratorLoginPassword string 

resource server 'Microsoft.DBforPostgreSQL/servers@2017-12-01' = {
  location:location
  name:serverName
  sku:{
    capacity: 2
    family: 'Gen5'
    name: 'GP_Gen5_2'
    size: 'string'
    tier: 'Basic'
  }
  properties:{
    createMode:'Default'
    administratorLogin:administratorLogin
    administratorLoginPassword:administratorLoginPassword
    sslEnforcement:'Enabled'
    version:'11'
    storageProfile:{
      storageMB:51200
      storageAutogrow:'Enabled'
    }
  }
}
