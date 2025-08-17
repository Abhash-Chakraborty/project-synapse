"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../components/ui/card"
import { Button } from "../components/ui/button"
import { Badge } from "../components/ui/badge"
import { Textarea } from "../components/ui/textarea"
import { DashboardStats } from "../components/dashboard-stats"
import { ActivityMonitor } from "../components/activity-monitor"
import { ToolUsageChart } from "../components/tool-usage-chart"
import { AgentInterface } from "../components/agent-interface"
import { BarChart3, Activity, Settings, RefreshCw, Zap, Bot } from "lucide-react"

export default function HomePage() {
  const [view, setView] = useState<'dashboard' | 'agent'>('dashboard')

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b bg-card sticky top-0 z-50">
        <div className="container mx-auto px-2 sm:px-4 py-3 sm:py-4">
          <div className="flex flex-col space-y-3 md:flex-row md:items-center md:justify-between md:space-y-0">
            {/* Logo and Title */}
            <div className="flex items-center gap-2 sm:gap-3">
              <div className="flex items-center justify-center w-8 h-8 md:w-10 md:h-10 bg-primary rounded-lg flex-shrink-0">
                <Zap className="h-4 w-4 md:h-6 md:w-6 text-primary-foreground" />
              </div>
              <div className="min-w-0 flex-1">
                <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-foreground truncate">Project Synapse</h1>
                <p className="text-xs md:text-sm text-muted-foreground hidden sm:block">AI-Powered Delivery Coordination System</p>
                <p className="text-xs text-muted-foreground sm:hidden">AI Delivery System</p>
              </div>
            </div>
            
            {/* Navigation and Status */}
            <div className="flex flex-col space-y-2 sm:flex-row sm:items-center sm:space-y-0 sm:space-x-2 md:space-x-3">
              {/* Navigation Buttons */}
              <div className="flex items-center gap-1 sm:gap-2">
                <Button 
                  variant={view === 'dashboard' ? 'default' : 'outline'} 
                  size="sm"
                  onClick={() => setView('dashboard')}
                  className="flex-1 sm:flex-none text-xs sm:text-sm px-3 py-2"
                >
                  <BarChart3 className="h-3 w-3 sm:h-4 sm:w-4 mr-1 sm:mr-2" />
                  <span className="hidden xs:inline">Dashboard</span>
                  <span className="xs:hidden">Dash</span>
                </Button>
                <Button 
                  variant={view === 'agent' ? 'default' : 'outline'} 
                  size="sm"
                  onClick={() => setView('agent')}
                  className="flex-1 sm:flex-none text-xs sm:text-sm px-3 py-2"
                >
                  <Bot className="h-3 w-3 sm:h-4 sm:w-4 mr-1 sm:mr-2" />
                  <span className="hidden xs:inline">Agent</span>
                  <span className="xs:hidden">AI</span>
                </Button>
              </div>
              
              {/* Status Badge */}
              <Badge variant="outline" className="text-emerald-600 border-emerald-200 self-start sm:self-auto whitespace-nowrap">
                <Activity className="h-3 w-3 mr-1 flex-shrink-0" />
                <span className="text-xs">Live</span>
              </Badge>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-2 sm:px-4 py-4 sm:py-6">
        {view === 'dashboard' ? <DashboardView /> : <AgentInterface />}
      </div>
    </div>
  )
}

function DashboardView() {
  const [lastRefresh, setLastRefresh] = useState(new Date())

  const handleRefresh = () => {
    setLastRefresh(new Date())
  }

  // Mock data
  const activities = [
    {
      id: "1",
      type: "case_resolved" as const,
      title: "Damaged Package Case Resolved",
      description: "Customer refund processed for Pizza Palace order",
      timestamp: new Date(Date.now() - 5 * 60 * 1000),
      status: "success" as const,
    },
    {
      id: "2",
      type: "tool_executed" as const,
      title: "Address Updated",
      description: "Delivery address corrected for vague location",
      timestamp: new Date(Date.now() - 12 * 60 * 1000),
      status: "success" as const,
    },
    {
      id: "3",
      type: "agent_response" as const,
      title: "AI Agent Analysis Complete",
      description: "Merchant overload scenario analyzed and resolved",
      timestamp: new Date(Date.now() - 18 * 60 * 1000),
      status: "info" as const,
    },
  ]

  const toolUsage = [
    {
      name: "Contact Customer",
      count: 45,
      successRate: 92,
      avgExecutionTime: "2.3s",
    },
    {
      name: "Get Merchant Status",
      count: 38,
      successRate: 96,
      avgExecutionTime: "1.8s",
    },
    {
      name: "Update Delivery Address",
      count: 32,
      successRate: 89,
      avgExecutionTime: "3.1s",
    },
  ]

  return (
    <div className="space-y-6">
      {/* Dashboard Stats */}
      <DashboardStats
        totalCases={156}
        resolvedCases={142}
        avgResolutionTime="4.2 min"
        successRate={91}
        activeAgents={3}
        toolsExecuted={183}
      />

      {/* Activity and Tool Usage */}
      <div className="grid gap-4 lg:gap-6 xl:grid-cols-2">
        <ActivityMonitor activities={activities} />
        <ToolUsageChart toolUsage={toolUsage} />
      </div>

      {/* System Overview */}
      <div className="grid gap-4 sm:gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle className="text-base sm:text-lg">System Health</CardTitle>
            <CardDescription className="text-xs sm:text-sm">Overall system performance</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-xs sm:text-sm">API Response Time</span>
              <Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200 text-xs">
                1.2s
              </Badge>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-xs sm:text-sm">Uptime</span>
              <span className="text-xs sm:text-sm font-medium">99.9%</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-xs sm:text-sm">Error Rate</span>
              <span className="text-xs sm:text-sm font-medium">0.1%</span>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-base sm:text-lg">Today's Summary</CardTitle>
            <CardDescription className="text-xs sm:text-sm">Key metrics for today</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-xs sm:text-sm">Cases Handled</span>
              <span className="text-xs sm:text-sm font-medium">23</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-xs sm:text-sm">Tools Executed</span>
              <span className="text-xs sm:text-sm font-medium">67</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-xs sm:text-sm">Evidence Collected</span>
              <span className="text-xs sm:text-sm font-medium">12</span>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Quick Actions</CardTitle>
            <CardDescription>System management</CardDescription>
          </CardHeader>
          <CardContent className="space-y-2">
            <Button variant="outline" size="sm" className="w-full justify-start bg-transparent" onClick={handleRefresh}>
              <RefreshCw className="h-4 w-4 mr-2" />
              Refresh Data
            </Button>
            <Button variant="outline" size="sm" className="w-full justify-start bg-transparent">
              <Settings className="h-4 w-4 mr-2" />
              System Configuration
            </Button>
            <Button variant="outline" size="sm" className="w-full justify-start bg-transparent">
              <Activity className="h-4 w-4 mr-2" />
              Export Activity Log
            </Button>
          </CardContent>
        </Card>
      </div>

      {/* Last Updated */}
      <div className="text-center text-sm text-muted-foreground">
        Last updated: {lastRefresh.toLocaleString()}
      </div>
    </div>
  )
}
