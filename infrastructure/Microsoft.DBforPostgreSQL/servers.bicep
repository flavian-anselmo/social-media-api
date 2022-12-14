param location string
param serverName string 

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
    name: 'B_Gen5_2'
    size: '5120'
    tier: 'Basic'
  }
  properties:{
    createMode:'Default'
    administratorLogin:administratorLogin
    administratorLoginPassword:administratorLoginPassword
    sslEnforcement:'Enabled'
    version:'11'
    storageProfile:{
      storageMB:5120
      storageAutogrow:'Disabled'
    }
  }
}
