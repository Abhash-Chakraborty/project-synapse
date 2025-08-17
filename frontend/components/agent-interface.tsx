"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Textarea } from "@/components/ui/textarea"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Bot, Send, Clock, CheckCircle, AlertCircle, Loader2, Zap } from "lucide-react"

interface AgentExecution {
  id: string
  scenario: string
  reasoning: string
  plannedActions: Array<{
    tool: string
    params: any
    reasoning: string
  }>
  executionResults: Array<{
    tool: string
    params: any
    reasoning: string
    result: any
    status: 'success' | 'error'
    error?: string
  }>
  timestamp: Date
  success: boolean
}

export function AgentInterface() {
  const [scenario, setScenario] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [executions, setExecutions] = useState<AgentExecution[]>([])

  const sampleScenarios = [
    "A restaurant is overloaded with a 40-minute kitchen prep time. Order ID: ORD-123, Customer: John Doe",
    "Damaged packaging dispute - spilled drink at customer's doorstep. Order ID: ORD-456, Driver: Mike Smith",
    "Recipient unavailable for valuable package delivery. Package ID: PKG-789, Location: Office Complex Downtown",
    "Major traffic obstruction blocking route to airport. Passenger has urgent flight FL-ABC123 departing in 90 minutes"
  ]

  const handleSubmitScenario = async () => {
    if (!scenario.trim()) return

    setIsLoading(true)
    const executionId = `exec_${Date.now()}`

    try {
      // Call the MCP server through Next.js API proxy
      const response = await fetch('/api/mcp/agent', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          scenario: scenario.trim(),
          context: {
            timestamp: new Date().toISOString(),
            executionId
          }
        })
      })

      const result = await response.json()

      console.log('MCP Response:', result) // Debug log

      if (response.ok) {
        const newExecution: AgentExecution = {
          id: executionId,
          scenario: scenario.trim(),
          reasoning: result.agent_reasoning || "No reasoning provided",
          plannedActions: result.planned_actions || [],
          executionResults: result.execution_results || [],
          timestamp: new Date(),
          success: result.success
        }

        console.log('New Execution:', newExecution) // Debug log
        setExecutions(prev => [newExecution, ...prev])
        setScenario("")
      } else {
        console.error('Agent execution failed:', result.error)
        // Create a mock execution for testing if server fails
        const mockExecution: AgentExecution = {
          id: executionId,
          scenario: scenario.trim(),
          reasoning: "MCP Server connection failed. This is a mock response for testing.",
          plannedActions: [
            {
              tool: "notify_customer",
              params: { customerId: "CUST_001", message: "Test message", voucher: 5 },
              reasoning: "Mock action for testing UI"
            }
          ],
          executionResults: [
            {
              tool: "notify_customer",
              params: { customerId: "CUST_001", message: "Test message", voucher: 5 },
              reasoning: "Mock action for testing UI",
              result: {
                customer_id: "CUST_001",
                notification_sent: true,
                message: "Test message",
                voucher_amount: 5,
                timestamp: new Date().toISOString()
              },
              status: 'success'
            }
          ],
          timestamp: new Date(),
          success: false
        }
        setExecutions(prev => [mockExecution, ...prev])
        setScenario("")
      }
    } catch (error) {
      console.error('Failed to execute scenario:', error)
      // Create a mock execution for testing when fetch fails
      const mockExecution: AgentExecution = {
        id: executionId,
        scenario: scenario.trim(),
        reasoning: "Network error occurred. This is a mock response to test the UI.",
        plannedActions: [
          {
            tool: "check_traffic",
            params: { location: "test_location" },
            reasoning: "Mock traffic check for testing"
          },
          {
            tool: "get_merchant_status", 
            params: { merchantId: "MERCH_001" },
            reasoning: "Mock merchant status check"
          }
        ],
        executionResults: [
          {
            tool: "check_traffic",
            params: { location: "test_location" },
            reasoning: "Mock traffic check for testing",
            result: {
              location: "test_location",
              condition: "moderate",
              estimated_delay_minutes: 5,
              alternative_routes_available: true
            },
            status: 'success'
          },
          {
            tool: "get_merchant_status",
            params: { merchantId: "MERCH_001" },
            reasoning: "Mock merchant status check",
            result: {
              merchant_id: "MERCH_001",
              status: "busy",
              estimated_prep_time_minutes: 20,
              order_queue_length: 5
            },
            status: 'success'
          }
        ],
        timestamp: new Date(),
        success: true
      }
      setExecutions(prev => [mockExecution, ...prev])
      setScenario("")
    } finally {
      setIsLoading(false)
    }
  }

  const loadSampleScenario = (sample: string) => {
    setScenario(sample)
  }

  return (
    <div className="space-y-6">
      {/* Agent Input Interface */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Bot className="h-5 w-5" />
            AI Agent Interface
          </CardTitle>
          <CardDescription>
            Describe a delivery disruption scenario and watch the AI agent reason through and resolve it
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <label htmlFor="scenario" className="text-sm font-medium">
              Disruption Scenario
            </label>
            <Textarea
              id="scenario"
              placeholder="Describe a delivery disruption scenario in detail..."
              value={scenario}
              onChange={(e) => setScenario(e.target.value)}
              className="min-h-[100px]"
            />
          </div>
          
          <div className="space-y-2">
            <p className="text-sm font-medium">Sample Scenarios:</p>
            <div className="grid gap-2 sm:grid-cols-2">
              {sampleScenarios.map((sample, index) => (
                <Button
                  key={index}
                  variant="outline"
                  size="sm"
                  className="h-auto p-2 sm:p-3 text-left justify-start text-wrap"
                  onClick={() => loadSampleScenario(sample)}
                >
                  <div className="text-xs leading-relaxed">{sample}</div>
                </Button>
              ))}
            </div>
          </div>

          <Button 
            onClick={handleSubmitScenario} 
            disabled={!scenario.trim() || isLoading}
            className="w-full"
          >
            {isLoading ? (
              <>
                <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                Agent Processing...
              </>
            ) : (
              <>
                <Send className="h-4 w-4 mr-2" />
                Execute Scenario
              </>
            )}
          </Button>
        </CardContent>
      </Card>

      {/* Execution History */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Clock className="h-5 w-5" />
            Execution History
          </CardTitle>
          <CardDescription>
            Previous agent executions and their results
          </CardDescription>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[600px]">
            {executions.length === 0 ? (
              <div className="text-center text-muted-foreground py-8">
                <Bot className="h-8 w-8 mx-auto mb-2 opacity-50" />
                <p>No executions yet. Try submitting a scenario above.</p>
              </div>
            ) : (
              <div className="space-y-4">
                {executions.map((execution) => (
                  <div key={execution.id} className="border rounded-lg p-4 space-y-4">
                    {/* Execution Header */}
                    <div className="flex items-start justify-between">
                      <div className="space-y-1">
                        <h3 className="font-medium text-sm">Scenario</h3>
                        <p className="text-sm text-muted-foreground">{execution.scenario}</p>
                      </div>
                      <div className="flex items-center gap-2">
                        <Badge 
                          variant={execution.success ? "default" : "destructive"}
                          className="flex items-center gap-1"
                        >
                          {execution.success ? (
                            <CheckCircle className="h-3 w-3" />
                          ) : (
                            <AlertCircle className="h-3 w-3" />
                          )}
                          {execution.success ? "Success" : "Failed"}
                        </Badge>
                        <span className="text-xs text-muted-foreground">
                          {execution.timestamp.toLocaleTimeString()}
                        </span>
                      </div>
                    </div>

                    {/* Agent Reasoning */}
                    <div className="space-y-2">
                      <h4 className="font-medium text-sm flex items-center gap-2">
                        <Bot className="h-4 w-4" />
                        Agent Reasoning
                      </h4>
                      <p className="text-sm bg-muted p-3 rounded italic">
                        "{execution.reasoning}"
                      </p>
                    </div>

                    {/* Planned Actions */}
                    {execution.plannedActions.length > 0 && (
                      <div className="space-y-2">
                        <h4 className="font-medium text-sm">Planned Actions</h4>
                        <div className="space-y-2">
                          {execution.plannedActions.map((action, index) => (
                            <div key={index} className="bg-muted p-3 rounded text-sm">
                              <div className="flex items-center gap-2 mb-1">
                                <Zap className="h-3 w-3" />
                                <span className="font-medium">{action.tool}</span>
                              </div>
                              <p className="text-muted-foreground text-xs mb-2">{action.reasoning}</p>
                              <div className="text-xs">
                                <span className="font-medium">Parameters:</span>
                                <pre className="mt-1 bg-background p-2 rounded text-xs overflow-x-auto">
                                  {JSON.stringify(action.params, null, 2)}
                                </pre>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Execution Results */}
                    {execution.executionResults.length > 0 && (
                      <div className="space-y-2">
                        <h4 className="font-medium text-sm">Execution Results</h4>
                        <div className="space-y-2">
                          {execution.executionResults.map((result, index) => (
                            <div key={index} className="border p-3 rounded text-sm">
                              <div className="flex items-center justify-between mb-2">
                                <div className="flex items-center gap-2">
                                  <Zap className="h-3 w-3" />
                                  <span className="font-medium">{result.tool}</span>
                                </div>
                                <Badge 
                                  variant={result.status === 'success' ? "default" : "destructive"}
                                  className="text-xs"
                                >
                                  {result.status}
                                </Badge>
                              </div>
                              {result.error ? (
                                <p className="text-red-600 text-xs">{result.error}</p>
                              ) : (
                                <div className="text-xs space-y-2">
                                  <div>
                                    <span className="font-medium">Tool Execution Info:</span>
                                    <pre className="mt-1 bg-muted p-2 rounded text-xs overflow-x-auto">
                                      {JSON.stringify({
                                        tool: result.tool,
                                        status: result.status,
                                        hasResult: 'result' in result,
                                        resultType: result.result ? typeof result.result : 'no result',
                                        reasoning: result.reasoning
                                      }, null, 2)}
                                    </pre>
                                  </div>
                                  <div>
                                    <span className="font-medium">Full Result Object:</span>
                                    <pre className="mt-1 bg-muted p-2 rounded text-xs overflow-x-auto">
                                      {JSON.stringify(result, null, 2)}
                                    </pre>
                                  </div>
                                </div>
                              )}
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </ScrollArea>
        </CardContent>
      </Card>
    </div>
  )
}
