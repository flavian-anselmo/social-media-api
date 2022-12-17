

param srcControlName string = 'src'
param repoUrl string = 'https://github.com/flavian-anselmo/social-media-api'
param branch string = 'main'
param runTimeVersion string = 'PYTHON|3.10'
param runTimeStack string = 'PYTHON'





resource srcControls 'Microsoft.Web/sites/sourcecontrols@2022-03-01' = {
  name: srcControlName
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
