param socialmediaPlanName string 
param location string 
param siteName string 
param linuxFxVersion string  



// server information (set this in a key vault)
param ALGORITHM string
param DATABASE_HOST string 
param DATABASE_NAME string 
param DATABASE_PASSWORD string
param DATABASE_PORT string 
param DATABASE_USERNAME string
param SECRET_KEY string 


@description('')
resource appServicePlan'Microsoft.Web/serverfarms@2022-03-01'existing ={
  name:socialmediaPlanName
}



@description('')
resource appService 'Microsoft.Web/sites@2022-03-01'={
  location:location
  name:siteName
  
  dependsOn:[
    appServicePlan
  ]
  properties:{
    serverFarmId:appServicePlan.id
    httpsOnly:true
    siteConfig: {
      linuxFxVersion: linuxFxVersion
    
      appSettings:[
        {
          name:'ALGORITHM'
          value:ALGORITHM
        }

        {
          name:'DATABASE_HOST'
          value: DATABASE_HOST
        }

        {
          name:'DATABASE_NAME'
          value: DATABASE_NAME
        }

        {
          name:'DATABASE_PASSWORD'
          value: DATABASE_PASSWORD
        }

        {
          name:'DATABASE_PORT'
          value:DATABASE_PORT
        }

        {
          name:'DATABASE_USERNAME'
          value: DATABASE_USERNAME
        }

        {
          name:'SECRET_KEY'
          value: SECRET_KEY
        }
        
      ]
    }
  }
  
}
