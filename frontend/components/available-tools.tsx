"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { ScrollArea } from "@/components/ui/scroll-area"
import { 
  Truck, 
  Users, 
  Scale, 
  Shield, 
  MapPin, 
  MessageSquare, 
  Package, 
  CheckCircle,
  AlertTriangle,
  RefreshCw,
  Camera,
  DollarSign,
  UserCheck,
  MessageCircle,
  QrCode,
  Navigation
} from "lucide-react"

interface Tool {
  name: string
  description: string
  category: 'logistics' | 'customer' | 'dispute' | 'verification'
  icon: React.ComponentType<any>
}

const tools: Tool[] = [
  // Logistics Tools
  {
    name: "get_merchant_status",
    description: "Check restaurant operational status and preparation times",
    category: "logistics",
    icon: Package
  },
  {
    name: "check_traffic",
    description: "Analyze route conditions and traffic patterns",
    category: "logistics",
    icon: Navigation
  },
  {
    name: "reroute_driver",
    description: "Optimize driver assignments and routes",
    category: "logistics",
    icon: Truck
  },
  {
    name: "get_nearby_merchants",
    description: "Find alternative vendors of similar cuisine",
    category: "logistics",
    icon: MapPin
  },
  
  // Customer Tools
  {
    name: "notify_customer",
    description: "Send notifications and updates to customers",
    category: "customer",
    icon: MessageSquare
  },
  {
    name: "contact_recipient_via_chat",
    description: "Initiate real-time chat with delivery recipients",
    category: "customer",
    icon: MessageCircle
  },
  {
    name: "suggest_safe_drop_off",
    description: "Recommend secure delivery locations",
    category: "customer",
    icon: Shield
  },
  {
    name: "find_nearby_locker",
    description: "Locate parcel lockers near delivery address",
    category: "customer",
    icon: Package
  },
  {
    name: "request_address_clarification",
    description: "Request clearer address details from customers",
    category: "customer",
    icon: MapPin
  },
  
  // Dispute Tools
  {
    name: "initiate_mediation_flow",
    description: "Start dispute resolution between parties",
    category: "dispute",
    icon: Scale
  },
  {
    name: "collect_evidence",
    description: "Gather photos and statements for disputes",
    category: "dispute",
    icon: Camera
  },
  {
    name: "analyze_evidence",
    description: "Determine fault and resolution based on evidence",
    category: "dispute",
    icon: AlertTriangle
  },
  {
    name: "issue_instant_refund",
    description: "Process immediate refunds for customers",
    category: "dispute",
    icon: DollarSign
  },
  {
    name: "exonerate_driver",
    description: "Clear driver of fault in dispute cases",
    category: "dispute",
    icon: UserCheck
  },
  {
    name: "log_merchant_packaging_feedback",
    description: "Record packaging quality feedback for merchants",
    category: "dispute",
    icon: MessageSquare
  },
  
  // Verification Tools
  {
    name: "verify_delivery_attempt",
    description: "Validate delivery attempts using GPS data",
    category: "verification",
    icon: CheckCircle
  },
  {
    name: "initiate_qr_code_verification",
    description: "Generate secure QR codes for delivery confirmation",
    category: "verification",
    icon: QrCode
  }
]

const categoryColors = {
  logistics: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
  customer: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  dispute: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
  verification: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200"
}

const categoryIcons = {
  logistics: Truck,
  customer: Users,
  dispute: Scale,
  verification: Shield
}

export function AvailableTools() {
  const groupedTools = tools.reduce((acc, tool) => {
    if (!acc[tool.category]) {
      acc[tool.category] = []
    }
    acc[tool.category].push(tool)
    return acc
  }, {} as Record<string, Tool[]>)

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-base sm:text-lg flex items-center gap-2">
          <RefreshCw className="h-4 w-4" />
          Available Tools ({tools.length} Total)
        </CardTitle>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-[400px] pr-4">
          <div className="space-y-4">
            {Object.entries(groupedTools).map(([category, categoryTools]) => {
              const CategoryIcon = categoryIcons[category as keyof typeof categoryIcons]
              return (
                <div key={category} className="space-y-2">
                  <div className="flex items-center gap-2">
                    <CategoryIcon className="h-4 w-4" />
                    <h3 className="font-medium capitalize text-sm">
                      {category} Tools ({categoryTools.length})
                    </h3>
                  </div>
                  <div className="space-y-2">
                    {categoryTools.map((tool) => {
                      const ToolIcon = tool.icon
                      return (
                        <div
                          key={tool.name}
                          className="flex items-start gap-3 p-2 rounded-lg border bg-muted/50"
                        >
                          <ToolIcon className="h-4 w-4 mt-0.5 flex-shrink-0" />
                          <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2 mb-1">
                              <code className="text-xs bg-muted px-1 py-0.5 rounded font-mono">
                                {tool.name}
                              </code>
                              <Badge 
                                variant="secondary" 
                                className={`text-xs ${categoryColors[tool.category]}`}
                              >
                                {category}
                              </Badge>
                            </div>
                            <p className="text-xs text-muted-foreground">
                              {tool.description}
                            </p>
                          </div>
                        </div>
                      )
                    })}
                  </div>
                </div>
              )
            })}
          </div>
        </ScrollArea>
      </CardContent>
    </Card>
  )
}
