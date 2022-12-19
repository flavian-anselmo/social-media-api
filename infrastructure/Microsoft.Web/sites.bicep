param socialmediaPlanName string = 'social-media-linux-service-plan'
param location string = 'eastus'
param siteName string = 'social-media-api'
param linuxFxVersion string  = 'PYTHON|3.10'



// server information (set this in a key vault)
param ALGORITHM string = 'HS256'
param DATABASE_HOST string = 'socialmedia-sandbox-server.postgres.database.azure.com'
param DATABASE_NAME string = 'social-media-api-db'
param DATABASE_PASSWORD string = 'rubyrails2005/'
param DATABASE_PORT string = '5432'
param DATABASE_USERNAME string = 'anselmo@socialmedia-sandbox-server'
param SECRET_KEY string = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'


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
