"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Activity, Clock, CheckCircle, AlertTriangle, PenToolIcon as Tool, MessageSquare } from "lucide-react"

interface ActivityItem {
  id: string
  type: "case_resolved" | "tool_executed" | "agent_response" | "system_alert"
  title: string
  description: string
  timestamp: Date
  status: "success" | "warning" | "error" | "info"
}

interface ActivityMonitorProps {
  activities: ActivityItem[]
}

const getActivityIcon = (type: string) => {
  const iconMap: Record<string, any> = {
    case_resolved: CheckCircle,
    tool_executed: Tool,
    agent_response: MessageSquare,
    system_alert: AlertTriangle,
  }

  const IconComponent = iconMap[type] || Activity
  return <IconComponent className="h-4 w-4" />
}

const getStatusColor = (status: string) => {
  switch (status) {
    case "success":
      return "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200"
    case "warning":
      return "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200"
    case "error":
      return "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200"
    case "info":
      return "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200"
    default:
      return "bg-muted text-muted-foreground"
  }
}

export function ActivityMonitor({ activities }: ActivityMonitorProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Activity className="h-5 w-5" />
          Recent Activity
        </CardTitle>
        <CardDescription>Real-time system activity and events</CardDescription>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-[300px] pr-4">
          <div className="space-y-3">
            {activities.length === 0 ? (
              <div className="text-center text-muted-foreground py-8">
                <Activity className="h-8 w-8 mx-auto mb-2 opacity-50" />
                <p>No recent activity</p>
              </div>
            ) : (
              activities.map((activity) => (
                <div key={activity.id} className="flex items-start gap-3 p-3 rounded-lg border bg-card">
                  <div className="flex items-center justify-center w-8 h-8 rounded-full bg-muted">
                    {getActivityIcon(activity.type)}
                  </div>
                  <div className="flex-1 space-y-1">
                    <div className="flex items-center justify-between">
                      <h4 className="text-sm font-medium">{activity.title}</h4>
                      <div className="flex items-center gap-2">
                        <Badge className={getStatusColor(activity.status)} variant="secondary">
                          {activity.status}
                        </Badge>
                        <span className="text-xs text-muted-foreground flex items-center gap-1">
                          <Clock className="h-3 w-3" />
                          {activity.timestamp.toLocaleTimeString()}
                        </span>
                      </div>
                    </div>
                    <p className="text-xs text-muted-foreground">{activity.description}</p>
                  </div>
                </div>
              ))
            )}
          </div>
        </ScrollArea>
      </CardContent>
    </Card>
  )
}
