"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { TrendingUp, TrendingDown, Package, Clock, CheckCircle, Users, Zap } from "lucide-react"
import { AvailableTools } from "../components/available-tools"

interface DashboardStatsProps {
  totalCases: number
  resolvedCases: number
  avgResolutionTime: string
  successRate: number
  activeAgents: number
  toolsExecuted: number
}

export function DashboardStats({
  totalCases,
  resolvedCases,
  avgResolutionTime,
  successRate,
  activeAgents,
  toolsExecuted,
}: DashboardStatsProps) {
  const pendingCases = totalCases - resolvedCases
  const resolutionRate = totalCases > 0 ? (resolvedCases / totalCases) * 100 : 0

  const stats = [
    {
      title: "Total Cases",
      value: totalCases.toString(),
      description: "Delivery disruptions handled",
      icon: Package,
      trend: "+12% from last week",
      trendUp: true,
    },
    {
      title: "Resolution Rate",
      value: `${resolutionRate.toFixed(1)}%`,
      description: `${resolvedCases} of ${totalCases} resolved`,
      icon: CheckCircle,
      trend: "+5.2% from last week",
      trendUp: true,
    },
    {
      title: "Avg Resolution Time",
      value: avgResolutionTime,
      description: "Time to resolve issues",
      icon: Clock,
      trend: "-8 min from last week",
      trendUp: true,
    },
    {
      title: "Success Rate",
      value: `${successRate}%`,
      description: "Customer satisfaction",
      icon: TrendingUp,
      trend: "+2.1% from last week",
      trendUp: true,
    },
  ]

  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat, index) => (
          <Card key={index}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">{stat.title}</CardTitle>
              <stat.icon className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stat.value}</div>
              <p className="text-xs text-muted-foreground">{stat.description}</p>
              <div className="flex items-center pt-1">
                {stat.trendUp ? (
                  <TrendingUp className="h-3 w-3 text-emerald-500 mr-1" />
                ) : (
                  <TrendingDown className="h-3 w-3 text-red-500 mr-1" />
                )}
                <span className={`text-xs ${stat.trendUp ? "text-emerald-600" : "text-red-600"}`}>{stat.trend}</span>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
      {/* Available Tools - takes 2 columns on large screens */}
      <div className="lg:col-span-2">
        <AvailableTools />
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Users className="h-4 w-4" />
              System Status
            </CardTitle>
            <CardDescription>Current system performance metrics</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-sm">Active Agents</span>
                <Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">
                  {activeAgents}
                </Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm">Tools Executed Today</span>
                <span className="text-sm font-medium">{toolsExecuted}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm">System Health</span>
                <Badge className="bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">
                  Optimal
                </Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Zap className="h-4 w-4" />
              Performance Metrics
            </CardTitle>
            <CardDescription>AI agent performance indicators</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-3">
              <div className="space-y-1">
                <div className="flex items-center justify-between text-sm">
                  <span>Response Accuracy</span>
                  <span className="font-medium">94%</span>
                </div>
                <Progress value={94} className="h-2" />
              </div>
              <div className="space-y-1">
                <div className="flex items-center justify-between text-sm">
                  <span>Tool Success Rate</span>
                  <span className="font-medium">89%</span>
                </div>
                <Progress value={89} className="h-2" />
              </div>
              <div className="space-y-1">
                <div className="flex items-center justify-between text-sm">
                  <span>Customer Satisfaction</span>
                  <span className="font-medium">{successRate}%</span>
                </div>
                <Progress value={successRate} className="h-2" />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
