param socialmediaPlanName string = 'social-media-linux-service-plan'
param location string = 'eastus'
param siteName string = 'social-media-api'
param linuxFxVersion string  = 'PYTHON|3.10'
param srcControlsName string = 'src'

@description('')
resource appServicePlan'Microsoft.Web/serverfarms@2022-03-01'existing ={
  name:socialmediaPlanName
}

@description('')
resource srcControls 'Microsoft.Web/sites/sourcecontrols@2022-03-01' = {
  name:srcControlsName
}

@description('')
resource appService 'Microsoft.Web/sites@2022-03-01'={
  location:location
  name:siteName
  
  dependsOn:[
    appServicePlan
    srcControls
  ]
  properties:{
    serverFarmId:appServicePlan.id
    httpsOnly:true
    siteConfig: {
      linuxFxVersion: linuxFxVersion
      appSettings:[
        {
          name:'ALGORITHM'
          value:'HS256'
        }

        {
          name:'DATABASE_HOST'
          value:'socialmedia-sandbox-server.postgres.database.azure.com'
        }
        {
          name:'DATABASE_NAME'
          value:'social-media-db'
        }

        {
          name:'DATABASE_PASSWORD'
          value:'rubyrails2005/'
        }

        {
          name:'DATABASE_PORT'
          value:'5432'
        }

        {
          name:'DATABASE_USERNAME'
          value:'anselmo@socialmedia-sandbox-server'
        }
        {
          name:'SECRET_KEY'
          value:'09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
        }
      ]
    }
  }
  
}
