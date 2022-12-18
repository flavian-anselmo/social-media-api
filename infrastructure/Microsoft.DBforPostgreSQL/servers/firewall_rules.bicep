/*
  DONE 

*/
param serverName string = 'socialmedia-sandbox-server'
param  firewallrules array= [
  
  {
    Name: 'ClientIPAddress_2022-12-17_11-25-24-rule_1'
    StartIpAddress: '196.201.218.144'
    EndIpAddress: '196.201.218.144'
  }
  {
    Name: 'AllowAll_2022-12-17_11-24-32-rule_2'
    StartIpAddress: '0.0.0.0'
    EndIpAddress: '255.255.255.255'
  }

]

resource server 'Microsoft.DBforPostgreSQL/servers@2017-12-01' existing = {
  name: serverName
}


@batchSize(2)
resource firewall 'Microsoft.DBforPostgreSQL/servers/firewallRules@2017-12-01' = [for rule in firewallrules: {
  name: '${server.name}-${rule.Name}'
  parent: server
  properties: {
    endIpAddress: rule.EndIpAddress
    startIpAddress: rule.StartIpAddress
  }
}]
