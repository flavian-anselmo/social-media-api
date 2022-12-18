
/*
 DONE 
 
*/
//param srcControlName string = 'srcControls'
param repoUrl string = 'https://github.com/flavian-anselmo/social-media-api'
param branch string = 'main'
param runTimeVersion string = 'PYTHON|3.10'
param runTimeStack string = 'PYTHON'
param appServiceName string = 'social-media-backend'

@description('')
resource appService 'Microsoft.Web/sites@2022-03-01' existing = {
  name:appServiceName
}



resource srcControls 'Microsoft.Web/sites/sourcecontrols@2022-03-01' = {
  name: 'web'
  parent: appService
  properties: {
    gitHubActionConfiguration:{
      generateWorkflowFile:true
      isLinux:true
      codeConfiguration:{
        runtimeStack:runTimeStack
        runtimeVersion:runTimeVersion
      }
    }
    repoUrl: repoUrl
    branch: branch
    isManualIntegration: true
    isMercurial:false
    isGitHubAction: true
  }
}
