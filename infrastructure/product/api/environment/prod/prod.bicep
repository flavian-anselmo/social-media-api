@secure()
param administratorLogin string 
@secure()
param administratorLoginPassword string 
@secure()
param DATABASE_PASSWORD string 
param socialmediaPlanName string = 'social-media-linux-service-plan'
param siteName string = 'social-media-api'
param linuxFxVersion string  = 'PYTHON|3.10'
param ALGORITHM string = 'HS256'
param DATABASE_HOST string = 'socialmedia-sandbox-server.postgres.database.azure.com'
param DATABASE_NAME string = 'social-media-api-db'
param DATABASE_PORT string = '8000'
param DATABASE_USERNAME string = 'anselmo@socialmedia-sandbox-server'
param SECRET_KEY string = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
param location_two string = 'westus3'
param serverName string = 'socialmedia-sandbox-server'
param location_one string   = 'eastus'
param operatingSys string = 'linux'
param skuName string  = 'B1'
param  socialMediaServicePlanName string = 'social-media-linux-service-plan'



module api '../../topology/prod/prod.bicep' = {
  name: 'api'
  params: {
    administratorLogin: administratorLogin
    administratorLoginPassword: administratorLoginPassword
    DATABASE_PASSWORD: DATABASE_PASSWORD
    ALGORITHM: ALGORITHM
    DATABASE_HOST: DATABASE_HOST
    DATABASE_NAME: DATABASE_NAME
    DATABASE_PORT: DATABASE_PORT
    DATABASE_USERNAME: DATABASE_USERNAME
    linuxFxVersion: linuxFxVersion
    location_one: location_one
    operatingSys: operatingSys
    SECRET_KEY: SECRET_KEY
    siteName: siteName
    skuName: skuName
    socialmediaPlanName: socialmediaPlanName
    socialMediaServicePlanName: socialMediaServicePlanName
    location_two: location_two
    serverName: serverName
  }
}
