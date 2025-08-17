"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { BarChart3 } from "lucide-react"

interface ToolUsage {
  name: string
  count: number
  successRate: number
  avgExecutionTime: string
}

interface ToolUsageChartProps {
  toolUsage: ToolUsage[]
}

export function ToolUsageChart({ toolUsage }: ToolUsageChartProps) {
  const maxCount = Math.max(...toolUsage.map((tool) => tool.count))

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <BarChart3 className="h-5 w-5" />
          Tool Usage Analytics
        </CardTitle>
        <CardDescription>Most frequently used delivery tools and their performance</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {toolUsage.map((tool, index) => (
            <div key={index} className="space-y-2">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="text-sm font-medium">{tool.name}</span>
                  <Badge variant="outline" className="text-xs">
                    {tool.count} uses
                  </Badge>
                </div>
                <div className="flex items-center gap-2 text-xs text-muted-foreground">
                  <span>{tool.successRate}% success</span>
                  <span>•</span>
                  <span>{tool.avgExecutionTime} avg</span>
                </div>
              </div>
              <div className="space-y-1">
                <Progress value={(tool.count / maxCount) * 100} className="h-2" />
                <div className="flex justify-between text-xs text-muted-foreground">
                  <span>Usage frequency</span>
                  <span>{((tool.count / maxCount) * 100).toFixed(0)}%</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  )
}
