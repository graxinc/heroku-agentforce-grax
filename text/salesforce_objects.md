Standard Objects
This section provides a list of standard objects and their standard fields.

Some fields may not be listed for some objects. To see the system fields for each object, see System Fields.

To verify the complete list of fields for an object, use a describe call from the API, or inspect with an appropriate tool. For example, inspecting the WSDL or using a schema viewer.

  AcceptedEventRelation
  Represents event participants (invitees or attendees) with the status Accepted for a given event.
  Account
  Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and partners).
  AccountBrand
  Represents the brand details of a Partner Account. This object is available in API version 43.0 and later.
  AccountContactRelation
  Represents a relationship between a contact and one or more accounts.
  AccountCleanInfo
  Stores the metadata Data.com Clean uses to determine an account record’s clean status. AccountCleanInfo helps you automate the cleaning or related processing of account records.
  AccountContactRole
  Represents the role that a Contact plays on an Account.
  AccountInsight
  Represents an individual insight (a key business development) related to an account record.
  AccountOwnerSharingRule
  Represents the rules for sharing an account with a User other than the owner.
  AccountPartner
  This object represents a partner relationship between two Account records. An AccountPartner record is created automatically when a Partner record is created for a partner relationship between two accounts. An AccountPartner record is also created automatically between an account and an opportunity’s account when a Partner record is created between an account and an opportunity.
  AccountPlan
  Represents customer information with measurable objectives and executable steps to proactively manage and grow customer relationships. This object is available in API version 62.0 and later.
  AccountPlanObjective
  Represents strategic objectives or initiatives pursued by a relationship team with a customer to enhance customer engagement and satisfaction. This object is available in API version 62.0 and later.
  AccountPlanObjectiveMeasure
  Represents the performance of target metrics for an objective associated with the account plan. This object is available in API version 62.0 and later.
  AccountPlanObjMeasCalcCond
  Represents a field and value combination for filtering records to include in the calculation of a sales account plan objective measure’s current value. This object is available in API version 63.0 and later.
  AccountPlanObjMeasCalcDef
  Represents the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective measure. This object is available in API version 63.0 and later.
  AccountPlanObjMeasCalcDefLocalization
  Represents the translated value of the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective measure. This object is available in API version 63.0 and later when the Translation Workbench is enabled.
  AccountRelationship
  Represents a relationship of a given type between two accounts. This object is available in API version 45.0 and later.
  AccountRelationshipShareRule
  Represents the rule that determines which object records are shared, how they are shared, the account relationship type that shares the records, and the level of access granted to the records. This object is available in API version 45.0 and later.
  AccountShare
  Represents a sharing entry on an account.
  AccountTag
  Associates a word or short phrase with an Account.
  AccountTeamMember
  Represents a User who is a member of an Account team.
  AccountTerritoryAssignmentRule
  An account assignment rule that assigns accounts to territories based on account fields. Available if Sales Territories has been enabled.
  AccountTerritoryAssignmentRuleItem
  A row of selection criteria for an AccountTerritoryAssignmentRule object. Available if Sales Territories has been enabled.
  AccountTerritorySharingRule
  Represents the rules for sharing an Account within a territory.
  AccountUserTerritory2View
  Represents the view of the Users in Assigned Territories related list in Lightning Experience for Sales Territories. Available in API version 42.0 and later.
  ActionCadence
  Represents the definition of a 1 cadence. This object is available in API version 45.0 and later.
  ActionCadenceRule
  Represents the logic that a branch step uses to determine which branch an action cadence tracker follows in an action cadence. Use ActionCadenceRule to learn about a branch step, including its logic and what the next step is. This object is available in API version 48.0 and later.
  ActionCadenceRuleCondition
  Represents the logic for a branch step. This object is available in API version 48.0 and later.
  ActionCadenceStep
  Represents a step in a cadence. Use ActionCadenceStep to learn which steps belong to a cadence, and how the steps are connected to each other. This object is available in API version 48.0 and later.
  ActionCadenceStepTracker
  Represents a step in an active cadence for a specific cadence target. This object is available in API version 48.0 and later.
  ActionCadenceStepVariant
  Represents an email template or call script variant associated with an action cadence step. Email and call steps can have up to 3 variants associated so sales teams can compare the engagement results. This object is available in API version 53.0 and later.
  ActionCadenceTracker
  Represents an active cadence target. This object is available in API version 45.0 and later.
  ActionCdncStpMonthlyMetric
  Represents the monthly engagement metrics for an action cadence step. This object is available in API version 49.0 and later.
  ActionLinkGroupTemplate
  Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed element. Clicking on an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external server or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. Every action link belongs to an action link group and action links within the group are mutually exclusive. This object is available in API version 33.0 and later.
  ActionLinkTemplate
  Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed element. Clicking an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external server or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. This object is available in API version 33.0 and later.
  ActionPlan
  Represents the instance of an action plan, a set of tasks created from an action plan template. This object is available in API version 44.0 and later.
  ActionPlanItem
  Represents the instance of an action plan item.This object is available in API version 44.0 and later.
  ActionPlanTemplate
  Represents the instance of an action plan template. This object is available in API version 44.0 and later.
  ActionPlanTemplateItem
  Represents the instance of an item on an action plan template version. This object is available in API version 44.0 and later.
  ActionPlanTemplateItemValue
  Represents the value associated with an action plan template item. This object is available in API version 44.0 and later.
  ActionPlanTemplateVersion
  Represents the version of an action plan template. This object is available in API version 44.0 and later.
  ActiveFeatureLicenseMetric
  Represents the number of active, assigned, and purchased feature licenses in the org. This object is available in API version 52.0 and later.
  ActivePermSetLicenseMetric
  Represents the number of active, assigned, and purchased permission set licenses in the org. This object is available in API version 52.0 and later.
  ActiveProfileMetric
  Represents the profile associated with the active, assigned, and purchased user licenses. This object is available in API version 52.0 and later.
  ActiveScratchOrg
  Represents an active scratch org. This object is available in API version 41.0 and later.
  ActivityFieldHistory
  Represents a change in a field value for a tracked object or field. This object is available in API version 55.0 and later.
  ActivityHistory
  This read-only object is displayed in a related list of closed activities—past events and closed tasks—related to an object. It includes activities for all contacts related to the object. ActivityHistory fields for phone calls are only available if your organization uses Salesforce CRM Call Center.
  ActivityMetric
  Represents activities that were added to Salesforce automatically by Einstein Activity Capture and manually by users.
  ActivityUsrConnectionStatus
  Represents the status of the email connections for Einstein Activity Capture users. You can also see whether users accepted the required terms of service to capture emails. This object is available in API version 54.0 and later.
  AdAvailabilityDimensions
  Table containing lookup references to specific objects with common, filterable fields between media types. This object is available in API version 59.0 and later.
  AdAvailabilityJob
  Stores batch job details that populate data in other aggregate tables. This object is available in API version 59.0 and later.
  AdAvailabilityViewConfig
  Represents configuration table for storing configurations, filters, and legend colors active in the calender view for corresponding pivots and media types. This object is available in API version 59.0 and later.
  AdBuyServerAccount
  Represents a user account in the buy side platform. The user can send RFPs to the seller and can accept, reject, or review proposals. For example, Buyer account. Every proposal in the Ad server requires both buyer and seller account details. This object is available in API version 59.0 and later.
  AdCreativeSizeType
  Defines the size of the Ad Creative. Example: 728 x 90 pixels. This object is available in API version 54.0 and later.
  AdDemographicCode
  Represents the demographic code details of an audience segment. This object is available in API version 60.0 and later.
  AdDigitalAvailability
  Table for Daily, Weekly, and Monthly view of offered, available, booked, and forecasted units for the Digital media type calendar view. This object is available in API version 59.0 and later.
  AdditionalNumber
  Represents an optional additional number for a call center. This additional number is visible in the call center's phone directory.
  Address
  Represents a mailing, billing, or home address.
  AdLinearAvailability
  Table for Daily, Weekly, and Monthly view of offered, available, booked, and forecasted units for the Linear media type calendar view. This object is available in API version 59.0 and later.
  AdOpportunity
  Represents an extension to the opportunity that stores campaign attributes specific to media ad sales. This object is available in API version 59.0 and later.
  AdOrderItem
  An extension to the Order LineItem and captures the details specific to an Ad Placement. This object is available in API version 54.0 and later.
  AdOrderItemCreativeSizeType
  Represents an intersection object between ad order item and ad creative size. It records companion creative sizes for each ad creative size and the number of times each parent creative needs to run. Users select this information in the media plan, which is then sent to the downstream execution system. This object is available in API version 59.0 and later.
  AdOrderLineAdTarget
  Represents the selections made by the user against a specific Ad Order Line item for a particular category. This object is available in API version 55.0 and later.
  AdOrderLineHiatus
  Represents the hiatus details of the media placement in a order line. This object is available in API version 60.0 and later.
  AdPageLayoutType
  Organize layouts for print, such as magazines and newspapers, or for screens, websites, applications, and much more. This object is available in API version 57.0 and later.
  AdProductTargetCategory
  An intersection table between Target Category and Product2. This object supports mapping the Target Category to all products, to a specific Media Type, or to a specific Product. This object is available in API version 55.0 and later.
  AdQuote
  An extension to Quote and captures quote attributes specific to Advertising Sales Management. This object is available in API version 54.0 and later.
  AdQuoteLine
  An extension to the Quote LineItem and captures the details specific to an Ad Placement. This object is available in API version 54.0 and later.
  AdQuoteLineCreativeSizeType
  Represents an intersection object between ad quote line and ad creative size. It records companion creative sizes for each ad creative size and the number of times each parent creative needs to run. Users select this information in the media plan, which is then sent to the downstream execution system. This object is available in API version 59.0 and later.
  AdQuoteLineAdTarget
  Represents the selections made by the user against a specific Ad Quote Line item for a particular category. This object is available in API version 55.0 and later.
  AdQuoteLineHiatus
  Represents the hiatus details of the media placement in a quote line. This object is available in API version 60.0 and later.
  AdServer
  Stores and delivers advertising content onto various platforms. This object is available in API version 54.0 and later.
  AdServerAccount
  Captures the mapping of an account with an Ad Server. This object is available in API version 54.0 and later.
  AdServerUser
  Captures the mapping of a User with an Ad Server. This object is available in API version 54.0 and later.
  AdSpaceCreativeSizeType
  Each Ad Space Creative Size Type defines the compatibility of an Ad Space with an Ad Creative Size Type. This object is available in API version 54.0 and later.
  AdSpaceGroupMember
  Defines the association of an Ad Space Specification record with an Ad Space Group record. This object is available in API version 54.0 and later.
  AdSpaceSpecification
  Defines a specific place or a group of places where an Ad Creative may be served. This object is available in API version 54.0 and later.
  AdSpecMediaPrintIssue
  Ad Specification Media Print Issue is a bridge entity that links the relationship between the Ad Space Specification and the Media Print Issue entities. This object is available in API version 57.0 and later.
  AdTargetCategory
  Represents an individual Targeting Category, which is used to group multiple targeting segments. This is mapped with Ad Server categories, containing the segments. For example, Audience Targeting and Geo targeting. This object is available in API version 55.0 and later.
  AdTargetCategorySegment
  Represents an individual Targeting Segment, which has available options among which selections can be made. For example, Gender, Education Demographics, Country, and State. This object is available in API version 55.0 and later.
  AgentWork
  Represents a work assignment that’s been routed to an agent. If the work is transferred to another agent, a new AgentWork record is created. This object is available in API version 32.0 and later.
  AgentWorkSkill
  Represents a skill used to route a work assignment to an agent. AgentWorkSkill is used for reporting and represents the result of a routing decision. This object is available in API version 42.0 and later.
  AIApplication
  Represents an AI application such as Einstein Prediction Builder. This object is available in API version 50.0 and later.
  AIApplicationConfig
  Additional prediction information related to an AI application. This object is available in API version 50.0 and later.
  AIInsightAction
  Represents an Einstein prediction insight action. This object is available in API version 47.0 and later.
  AIInsightFeedback
  Represents an Einstein prediction insight feedback. This object is available in API version 47.0 and later.
  AIInsightReason
  Represents an Einstein prediction insight reason. This object is available in API version 47.0 and later.
  AIInsightValue
  Represents an Einstein prediction insight value. This object is available in API version 47.0 and later.
  AiModelLanguage
  An object that stores language related information that is generated for each AI model. This object is available in API version 55.0 and later.
  AIRecordInsight
  Represents an Einstein prediction insight. This object is available in API version 47.0 and later.
  AllowedEmailDomain
  Represents an allowed email domain for users in your organization. You can define an allowlist to restrict the email domains allowed in a user’s Email field. This object is available in API version 29.0 and later.
  AlternativePaymentMethod
  Represents a payment method that isn’t cash, a debit card, or a credit card. This object defines methods that aren’t defined by the CardPaymentMethod or DigitalWallet objects. Examples of alternative payment methods include CashOnDeliver, Klarna, and Direct Debit. AlternativePaymentMethod functions the same as any other type of payment method for processing transactions through a payment gateway. This object is available in API version 51.0 and later.
  AnalyticsChangeEventLog
  Analytics Change Event Logs represent route or page changes made in the CRM Analytics. This object is available in API version 61.0 and later.
  AnalyticsDownloadEventLog
  AnalyticsDownloadEventLog represent downloads made from lens and dashboard in the CRM Analytics. This object is available in API version 61.0 and later.
  AnalyticsInteractEventLog
  Analytics Interact Event Log represents route or page changes made in the CRM Analytic UI. This object is available in API version 61.0 and later.
  AnalyticsLicensedAsset
  Represents a licensed Analytics asset. In this context, Analytics is CRM Analytics, Sonic, or Mulesoft Data Path. Available in API version 52.0 and later.
  AnalyticsPerfEventLog
  Analytics Perf Event Log helps track trends in your Analytics performance. This object is available in API version 61.0 and later.
  Announcement
  Represents a Chatter group announcement. This object is available in API version 30.0 and later.
  ApexCalloutEventLog
  Apex Callout event logs contain details about callouts (external requests) during Apex code execution. This object is available in API version 55.0 and later.
  ApexClass
  Represents an Apex class.
  ApexComponent
  Represents a definition for a custom component that can be used in a Visualforce page alongside standard components such as <apex:relatedList> and <apex:dataTable>.
  ApexExecutionEventLog
  Apex Execution event logs contain details about Apex classes that are used. This object is available in API version 55.0 and later.
  ApexExtlCalloutEventLog
  Apex Extl Callout EventLog represent external data callouts via custom adapters for Salesforce Connect. This object is available in API version 61.0 and later.
  ApexLog
  Represents a debug log containing information about a transaction, including information about Apex, Visualforce, and workflow and validation rules. This object is available in API version 19.0 and later.
  ApexPage
  Represents a single Visualforce page.
  ApexPageInfo
  Represents metadata about a single Visualforce page. This object is available in API version 48.0 and later.
  ApexRestApiEventLog
  Apex REST API event logs capture information about every Apex REST API request. This object is available in API version 55.0 and later.
  ApexSoapApiEventLog
  Apex SOAP event logs contain details about custom SOAP web service calls. This object is available in API version 55.0 and later.
  ApexTestQueueItem
  Represents a single Apex class in the Apex job queue. This object is available in API version 23.0 and later.
  ApexTestResult
  Represents the result of an Apex test method execution. This object is available in API version 23.0 and later.
  ApexTestResultLimits
  Captures the Apex test limits used for a particular test method execution. An instance of this object is associated with each ApexTestResult record. This object is available in API version 37.0 and later.
  ApexTestRunResult
  Contains summary information about all the test methods that were run in a particular Apex job. This object is available in API version 37.0 and later.
  ApexTestSuite
  Represents a suite of Apex classes to include in a test run. A TestSuiteMembership object associates each class with the suite. This object is available in API version 36.0 and later.
  ApexTrigger
  Represents an Apex trigger.
  ApexTriggerEventLog
  Apex Trigger event logs contain details about triggers that fire in an organization. This object is available in API version 55.0 and later.
  ApexTypeImplementor
  Represents Apex classes that directly or indirectly implement an interface. Using a SOQL query this object gets information about public or global classes and only global classes for installed managed packages. This object is available in API version 54.0 and later.
  ApexUnexpectedExcpEventLog
  Apex Unexpected Excp Event Log captures information about unexpected exceptions in Apex code execution. This object is available in API version 61.0 and later.
  ApiTotalUsageEventLog
  API Total Usage Event Log contains details about Platform SOAP API, Platform REST API, and Bulk API requests. This object is available in API version 61.0 and later.
  AppAnalyticsQueryRequest
  Represents a request for AppExchange App Analytics data.
  AppDefinition
  Represents the metadata of an app and its navigation items. Metadata is returned only for apps that the current user can access. This object is available in API version 43.0 and later.
  AppExtension
  Represents a connection between the Field Service mobile app and another app, typically for passing record data to the Salesforce mobile app or other apps. This object is available in API version 41.0 and later.
  ApplicationFormTemplate
  Represents the fields to capture application metadata as a template which is used in application tracking and processing. This object is available in API version 59.0 and later.
  AppMenuItem
  Represents the organization’s default settings for items in the app menu or App Launcher.
  AppointmentAssignmentPolicy
  Stores information about resource assignment rules. This object is available in API version 52.0 and later.
  AppointmentScheduleAggr
  Records the utilization of a service resource, by date, for the Load Balancing appointment assignment policy. This object is available in API version 52.0 and later.
  AppointmentScheduleLog
  Stores service appointments of each service Resource. This object is used to calculate the utilization of a service resource for the AppointmentScheduleAggr object. This object is available in API version 52.0 and later.
  AppointmentSchedulingPolicy
  Represents a set of rules for scheduling appointments using Salesforce Scheduler. This object is available in API version 45.0 and later.
  AppointmentTopicTimeSlot
  Represents a lookup to a work type or a work type group for a time slot This object is available in API version 52.0 and later.
  Approval
  Represents an approval request for a Contract.
  AppTabMember
  Represents the list of tabs for each of the available apps. This object is available in API version 43.0 and later.
  ApptBundleAggrDurDnscale
  Sums the duration of the bundle members, reduced by a predefined percentage. This object is available in API version 54.0 and later.
  ApptBundleAggrPolicy
  Policy that defines how the property values of the bundle members are aggregated and assigned to the bundle. This object is available in API version 54.0 and later.
  ApptBundleConfig
  Represents the general parameters that define the behavior of the bundle. This object is available in API version 54.0 and later.
  ApptBundlePolicy
  Policy that defines how the bundling of service appointments should be handled. This object is available in API version 54.0 and later.
  ApptBundlePolicySvcTerr
  Represents a link between the BundlePolicy and the ServiceTerritory. This object is available in API version 54.0 and later.
  ApptBundlePropagatePolicy
  Policy that defines which property values are inherited from the bundle to the bundle members or are assigned as constant values in the bundle members. This object is available in API version 55.0 and later.
  ApptBundleRestrictPolicy
  Policy that defines the restrictions that are considered while forming a bundle. This object is available in API version 54.0 and later.
  ApptBundleSortPolicy
  Policy that defines the properties by which the bundle members are sorted within the bundle. Can also be used in the automatic mode for determining the order of the automatic selection of bundle members. This object is available in API version 54.0 and later.
  AppUsageAssignment
  Provides application context for a record. A record can have different allowed actions or different related objects when it’s created for different applications. For example, a Subscription Management order has a related SubscriptionManagement AppUsageAssignment, so Salesforce knows it can create assets for that order. Available in API version 50.0 and later.
  Article Type__DataCategorySelection
  A data category selection represents a data category that classifies an article. This object is available in API version 19.0 and later.
  Asset
  Represents an item of commercial value, such as a product sold by your company or a competitor, that a customer has purchased.
  AssetAction
  Represents a change made to a lifecycle-managed asset. The fields can’t be edited. This object is available in API version 50.0 and later.
  AssetActionSource
  Represents an optional way to record what transactions caused changes to lifecycle-managed assets. Use it to trace financial and other information about asset actions. This object supports Salesforce order products and work order line items, and transaction IDs from other systems. The fields can’t be edited. This object is available in API version 50.0 and later.
  AssetAttribute
  Stores asset attributes to track and analyze asset conditions to improve their uptime. This object is available in API version 57.0 and later.
  AssetContractRelationship
  Represents a relationship between an asset and a contract. This object is available in API version 60.0 and later.
  AssetDowntimePeriod
  Represents a period during which an asset is not able to perform as expected. Downtime periods include planned activities, such as maintenance, and unplanned events, such as mechanical breakdown. This object is available in API version 49.0 and later.
  AssetOwnerSharingRule
  Represents the rules for sharing an Asset with users other than the owner. This object is available in API version 33.0 and later.
  AssetRateAdjustment
  Stores the tier rate adjustments for the asset rate card entries. This object is available in API version 62.0 and later.
  AssetRateCardEntry
  Stores the negotiated rate card entries that are associated with an asset in Revenue Cloud. This object is available in API version 62.0 and later.
  AssetRelationship
  Represents a non-hierarchical relationship between assets due to an asset modification; for example, a replacement, upgrade, or other circumstance. In Subscription Management and Revenue Lifecycle Management, this object represents an asset or assets grouped in a bundle or set. This object is available in API version 41.0 and later.
  AssetShare
  Represents a sharing entry on an Asset. This object is available in API version 33.0 and later.
  AssetStatePeriod
  Represents a time span when an asset has the same quantity, amount, and monthly recurring revenue (MRR). An asset has as many asset state periods as there are changes to it (asset actions) during its lifecycle. The dashboard and related pages show the current asset state period. The fields can’t be edited. This object is available in API version 50.0 and later.
  AssetStatePeriodAttribute
  Represents a virtual object that holds the key-value pair of the asset attribute in a specified asset state period. This object is a child object of AssetStatePeriod. This object is available in API version 60.0 and later.
  AssetTag
  Associates a word or short phrase with an Asset.
  AssetTokenEvent
  The documentation has moved to AssetTokenEvent in the Platform Events Developer Guide.
  AssetWarranty
  Defines the warranty terms applicable to an asset along with any exclusions and extensions. This object is available in API version 50.0 and later.
  AssignedResource
  Represents a service resource who is assigned to a service appointment in Field Service and Lightning Scheduler. Assigned resources appear in the Assigned Resources related list on service appointments. This object is available in API version 38.0 and later.
  AssignmentRule
  Represents an assignment rule associated with a Case or Lead.
  AssociatedLocation
  Represents a link between an account and a location in Field Service. You can associate multiple accounts with one location. For example, a shopping center location may have multiple customer accounts.
  AsyncApexJob
  Represents an individual Apex sharing recalculation job, a batch Apex job, a method with the future annotation, or a job that implements Queueable or Schedulable. Use this object to query Apex batch jobs in your organization.
  AsyncOperationLog
  Represents an async operations log containing progress and status information about external synchronizations to the Omnichannel Inventory service. This object is available in API version 51.0 and later.
  AsyncOperationTracker
  Represents the status of an asynchronous request initiated from the Quote, Order, and CreditMemo entities. This object is available in API version 61.0 and later.
  AttachedContentDocument
  This read-only object contains all ContentDocument objects associated with an object.
  AttachedContentNote
  This read-only object contains all ContentNote objects associated with an object. This object is available in API version 35.0 and later.
  Attachment
  Represents a file that a User has uploaded and attached to a parent object.
  AttributeDefinition
  Represents a product, asset, or object attribute, for example, a hardward specification or software detail. This object is available in API version 57.0 and later.
  AttributePicklist
  Represents a custom picklist for an asset attribute. This object is available in API version 57.0 and later.
  AttributePicklistValue
  Represents the values of an asset attribute picklist. This object is available in API version 57.0 and later.
  AsyncReportRunEventLog
  Async Report Run Event Log is used for reporting scheduled requests. This category includes dashboard refreshes, asynchronous reports, schedule reports, and analytics snapshots. This object is available in API version 61.0 and later.
  Audience
  Represents an audience that is defined by criteria and can be assigned and used for targeting in an Experience Cloud site. This object is available in API version 44.0 and later.
  AuraDefinition
  Represents an Aura component definition, such as component markup, a client-side controller, or an event. This object is available in API version 32.0 and later.
  AuraDefinitionBundle
  Represents a Lightning Aura component definition bundle, such as a component or application bundle. A bundle contains a Lightning Aura component definition and all its related resources. This object is available in API version 32.0 and later.
  AuraDefinitionBundleInfo
  For internal use only.
  AuraDefinitionInfo
  For internal use only.
  AuraRequestEventLog
  Aura Request Event Log contains details of requests to Apex methods from Aura and Lightning web components. This object is available in API version 61.0 and later.
  AuthConfig
  Represents authentication options for My Domain and Experience Cloud site login pages. This object is available in API version 32.0 and later.
  AuthConfigProviders
  Represents an authentication provider that’s configured in an organization. AuthConfigProviders is a child of the AuthConfig object. This object is available in API version 32.0 and later.
  AuthorizationForm
  Represents the specific version and effective dates of a form that is associated with consent, such as a privacy policy or terms and conditions. This object is available in API version 46.0 and later.
  AuthorizationFormConsent
  Represents the date and way in which a user consented to an authorization form. This object is available in API version 46.0 and later.
  AuthorizationFormDataUse
  Represents the data use consented to in an authorization form. This object is available in API version 46.0 and later.
  AuthorizationFormText
  Represents an authorization form’s text and language settings. This object is available in API version 46.0 and later.
  AuthProvider
  Represents an authentication provider (auth provider). An auth provider lets users log in to your Salesforce org from an external service provider, such as Facebook, Google, or GitHub. This object is available in API version 27.0 and later.
  AuthProvParamFwdAllowlist
  Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the authorization URL. Use this type to add custom functionality to authentication providers. For example, allowlist a ui_locales parameter and use it to send a user's language preference from Salesforce to the third-party provider's login page. This object is available in API version 62..0 and later.
  AuthSession
  The AuthSession object represents an individual user session in your organization. This object is available in versions 29.0 and later.
  AutomatedAction
  Represents the configuration of an automated action, such as a workflow rule. This object is available in API version 57.0 and later.
  AutomatedActionCondition
  Represents the logical operator details for evaluating conditions in an automated action. This object is available in API version 57.0 and later.
  AutomatedActionOverride
  Represents a modified attribute of a shared automated action. For example, the modified attribute can contain customizations for your business. This object is available in API version 58.0 and later.
  AutomatedActionParameter
  Represents the values or field references evaluated by the automated action. This object is available in API version 57.0 and later.
  AutomatedActionReminder
  Represents a reminder to the end user to take an action in the future. This object is available in API version 58.0 and later.
  BackgroundOperation
  Represents a background operation in an asynchronous job queue. This object is available in API version 35.0 and later.
  BackgroundOperationResult
  Stores error messages generated when or importing data into big objects using Bulk API. This is a big object, available in API version 37.0 and later.
  BatchApexErrorEvent
  The documentation has moved to BatchApexErrorEvent in the Platform Events Developer Guide.
  BillingBatchScheduler
  Represents a scheduled processing job that triggers recurring invoice batch runs and payment batch runs in Subscription Management. This object is available in API version 55.0 and later.
  BillingPeriodItem
  Represents one payment period for a subscription. The billing period item is used to pass billing information to an invoice line item in Subscription Management. This object is available in API version 55.0 and later.
  BillingPolicy
  Represents a group of billing treatments, which define the rules for how to invoice a customer for an order item. This object is available in API version 55.0 and later.
  BillingSchedule
  Stores the order item information used in the invoicing process. This object is available in API version 55.0 and later.
  BillingScheduleGroup
  Represents a consolidated view of all billing schedules related to the order items generated from one asset, including new orders and amendment orders. This object is available in API version 55.0 and later.
  BillingTreatment
  Defines how Subscription Management bills an order item. The Exclude From Billing field controls whether the order item is invoiced. Child billing treatment items control how much of the order item's balance is invoiced for each invoice across the subscription's lifecycle. Billing treatments are assigned to order items based on the parent billing policy's Billing Treatment Selection field. This object is available in API version 55.0 and later.
  BillingTreatmentItem
  A billing treatment item defines how the order item's total amount is distributed into billing schedules over the course of the order item's lifecycle. In the Subscription Management pilot, billing treatments must have only one billing treatment item, so that the billing treatment item covers 100% of the order item's total value. This object is available in API version 55.0 and later.
  Bookmark
  Represents a link between opportunities that share common information.
  BrandingSet
  Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience Builder. This object is available in API version 40.0 and later.
  BrandTemplate
  Letterhead for HTML EmailTemplate.
  Brief
  Represents a marketing brief. A brief contains information that’s used for positioning and grounding a marketing campaign. This object is available in API version 61.0 and later.
  BriefcaseAssignment
  Represents the assignment of a briefcase definition to selected users and user groups. This object is available in API version 50.0 and later.
  BriefcaseDefinition
  Represents a briefcase definition. A briefcase makes selected records available for users to view when they’re offline in the Salesforce Field Service mobile app for iOS and Android. This object is available in API version 50.0 and later.
  BriefcaseRule
  Represents a rule that specifies records for a briefcase definition. This object is available in API version 50.0 and later.
  BriefcaseRuleFilter
  Represents a filter criteria for a briefcase rule. This object is available in API version 50.0 and later.
  BroadcastCommAudience
  Represents the audience that the broadcast communication is sent to. This object is available in API version 56.0 and later.
  BroadcastCommunication
  Represents a broadcast communication related to an incident. This object is available in API version 56.0 and later.
  BroadcastTopic
  Represents a definition of a broadcast topic. A broadcast topic is associated with a list of Experience Cloud network sites for Service Cloud and collaboration rooms for Sales Cloud. The topic is created for a specific user role. Collaboration rooms are linked to Slack channels. This object is available in API version 55.0 and later.
  BroadcastTopicGroup
  Represents a junction object that relates a group to an alert type broadcast topic. The broadcast sends the alert to this group. This object is available in API version 57.0 and later.
  BroadcastTopicNetwork
  Represents a link between a broadcast topic and the Experience Cloud network site for Service Cloud. This object is available in API version 56.0 and later.
  BrowserPolicyViolation
  Represents a violation related to the Trusted URLs and Trusted URLs for External Redirects allowlists. These violations include blocked resource requests based on your content security policy (CSP) and blocked redirections. This object is available in API version 61.0 and later.
  BulkApi2EventLog
  Bulk API 2 event logs contain details about Bulk API 2.0 requests. This object is available in API version 61.0 and later.
  BulkApiEventLog
  Bulk API event logs contain details about Bulk API requests. This object is available in API version 55.0 and later.
  BusinessBrand
  Represents a unique brand for a business that belongs to a parent entity. This object is available in API version 53.0 and later.
  BusinessAlert
  Represents information about insight notifications that Einstein Relationship Insights explores, such as news mentions, job updates, and relationships. This object is available in API version 57.0 and later.
  BusinessAlertStatus
  Represents information about the read status of an insight alert. This object is available in API version 57.0 and later.
  BusinessHours
  Specifies the business hours of your support organization. Escalation rules are run only during these hours.
  BusinessProcess
  Represents a business process.
  BusinessProcessDefinition
  Setup object that stores information about stages in a customer lifecycle map. The stages are associated with surveys and questions created using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and later.
  BusinessProcessFeedback
  Setup object that stores information about the survey and the question associated with each stage in a customer lifecycle map. Customer lifecycle maps are used to track the scores provided by customers across their lifecycle using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and later.
  BusinessProcessGroup
  Setup object that stores information about customer lifecycle maps. Customer lifecycle maps are used to track the scores provided by customers across their lifecycle using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and later.
  BuyerAccount
  Represents an account that is enabled as a buyer for Lightning B2B Commerce. This object is available in API version 48.0 and later.
  BuyerCriteria
  Represents the buyer context qualifier of locale for any buyer groups of type Market This object is available in API version 58.0 and later.
  BuyerGroup
  Associates group qualifiers (entitlements, price books, promotions, and shipping methods) with buyer members based on buyer account ID or on the localized language and currency of the market browsed in a webstore. This object is available in API version 57.0; amended to support Market in version 58.0 and later.
  BuyerGroupBuyerCriteria
  Associates a buyer group that is enabled for webstores supporting multiple languages and currencies with BuyerCriteria that define those languages and currencies. This object is available in API version 58.0 and later.
  BuyerGroupMember
  Represents a member of a buyer group. This object is available in API version 55.0 and later.
  BuyerGroupPricebook
  Represents a buyer group price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.
  BuyerGroupRelatedObject
  Used to associate currencies and supported ship-to countries with a buyer group and its price books, promotions, and entitlements. Supports buyer experience when buyer group members shop in stores enabled for multiple locales. This object is available in API version 58.0 and later.
  CalcProcStepRelationship
  Defines a parent-child relationship between two Expression Set Steps in an Expression Set Version. The label for this object is Expression Set Step Relationship. This object is available in API version 53.0 and later.
  CalculatedInsightRangeBound
  Stores the information required to calculate a range-bound data insight. This object is available in API version 59.0 and later.
  CalculationMatrix
  Matches input values to a table row and returns the row's output values. The label for this object is Decision Matrix. This object is available in API version 53.0 and later.
  CalculationMatrixColumn
  Defines a column in a Decision Matrix. The label for this object is Decision Matrix Column. This object is available in API version 53.0 and later.
  CalculationMatrixRow
  Defines a row in a Decision Matrix. The label for this object is Decision Matrix Row. This object is available in API version 53.0 and later.
  CalculationMatrixVersion
  Defines a version of a Decision Matrix. The label for this object is Decision Matrix Version. This object is available in API version 53.0 and later.
  CalculationProcedure
  Performs a series of calculations using matrix lookups and user-defined variables and constants. The label for this object is Expression Set. This object is available in API version 53.0 and later.
  CalculationProcedureStep
  Defines a step in an Expression Set. The label for this object is Expression Set Step. This object is available in API version 53.0 and later.
  CalculationProcedureVariable
  Defines a variable in an Expression Set. The label for this object is Expression Set Variable. This object is available in API version 53.0 and later.
  CalculationProcedureVersion
  Defines a version of an Expression Set. The label for this object is Expression Set Version. This object is available in API version 53.0 and later.
  Calendar
  Represents a calendar. This can be a default user calendar, public calendar, resource calendar, or holiday calendar. This object is available in API version 45.0 and later.
  CalendarView
  These calendars can be created and assigned to users other than the creator. Available calendars include object, shared, public, resource, and user list calendars. Object calendars represent a calendar based on a Salesforce object, either standard or custom. This object is available in API version 51.0 and later.
  CallCenter
  Represents a call center, which is a logical representation of a single computer-telephony integration (CTI) system instance in an organization.
  CallCenterRoutingMap
  Stores a mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center. This object is available in API version 53.0 and later.
  CallCoachConfigModifyEvent
  Represents a Conversation Insights configuration change. This object is available in API version 49.0 and later.
  CallCoachingMediaProvider
  Represents the media provider for call recordings. This object is available in API version 49.0 and later.
  CallCtrAgentFavTrfrDest
  Represents a transfer destination that has been marked (starred) as a favorite in the Omni-Channel softphone by a contact center agent for voice call transfers. This object is available in API version 55.0 and later.
  CallCtrAgentFavTrfrDestShare
  Represents a sharing entry on a favorite transfer destination in the Omni-Channel softphone for voice call transfers. This object is available in API version 55.0 and later.
  CallDisposition
  Represents a call result value that sales reps select when logging a call. This object is available in API version 47.0 and later.
  CallDispositionCategory
  Represents the call outcome of a phone call that is used in reports and branching criteria for cadences. This object is available in API version 47.0 and later.
  CallTemplate
  Represents a call script for users to read when making calls.
  Campaign
  Represents and tracks a marketing campaign, such as a direct mail promotion, webinar, or trade show.
  CampaignInfluence
  Represents the association between a campaign and an opportunity in Customizable Campaign Influence. This object is available in API version 37.0 and later.
  CampaignInfluenceModel
  This read-only object represents a campaign influence model in Customizable Campaign Influence. Use campaign influence models to group CampaignInfluence records created by a specific set of triggers and workflows that you define. The Primary Campaign Source influence model is the default model. This object is available in API version 37.0 and later.
  CampaignMember
  The CampaignMember object represents the relationship between a campaign and either a lead or a contact. If the Accounts as Campaign Members setting is enabled in an org, CampaignMember can also represent the relationship between a campaign and an account.
  CampaignMemberStatus
  One or more member status values defined for a campaign.
  CampaignOwnerSharingRule
  Represents the rules for sharing a campaign with User records other than the owner or anyone above the owner in the role hierarchy.
  CampaignShare
  Represents a sharing entry on a Campaign.
  CampaignTag
  Associates a word or short phrase with a Campaign.
  CardPaymentMethod
  Represents a credit card or debit card payment method, which implements the PaymentMethod object. This object is available in API version 48.0 and later.
  CartCheckoutSession
  Represents a checkout session used in Lightning B2B Commerce checkout. This object is available in API version 48.0 and later.
  CartDeliveryGroup
  Represents shipping information for the delivery of items in an order against a store built with B2B Commerce or D2C Commerce. This object is available in API version 49.0 and later.
  CartDeliveryGroupMethod
  Represents the selected delivery method for a cart delivery group used in Lightning B2B Commerce checkout. This object is available in API version 49.0 and later.
  CartDeliveryGroupMethodAdj
  Represents the shipping promotion discount for a shipping method. This object is available in API version 60.0 and later.
  CartItem
  Represents an item in a WebCart that’s active in a store built with B2B or D2C Commerce. Cart item can be of type Product or Charge. This object is available in API version 49.0 and later.
  CartItemPriceAdjustment
  Price adjustment for a cart item. This object is available in API version 52.0 and later.
  CartTax
  Represents taxes for a line item in a WebCart that’s active in a store built with B2B Commerce or D2C Commerce. This object is available in API version 49.0 and later.
  CartValidationOutput
  Associate errors to cart entities, such as cart line items, delivery groups, and the like, in a store built with B2B Commerce or D2C Commerce. An example error is “Out of stock.” Available in API version 49.0 and later.
  Case
  Represents a case, which is a customer issue or problem.
  CaseArticle
  Represents the association between a Case and a KnowledgeArticle. This object is available in API version 20.0 and later.
  CaseComment
  Represents a comment that provides additional information about the associated Case.
  CaseContactRole
  Represents the role that a given Contact plays on a Case.
  CaseHistory
  Represents historical information about changes that have been made to the associated Case.
  CaseHistory2
  Represents historical information about owner and status changes that have been made to the associated Case. This object is available in API version 59.0 and later.
  CaseMilestone
  Represents a milestone (required step in a customer support process) on a Case. This object is available in API version 18.0 and later.
  CaseOwnerSharingRule
  Represents the rules for sharing a case with users other than the owner.
  CaseParticipant
  Represents a junction between a case, and an account or a contact. This object stores the details of the participant associated with a case. This participant could be the applicant, co-applicant, a household, or even a business account. This object is available in API version 54.0 and later.
  CaseRelatedIssue
  This object acts as a junction between a customer issue (Case) and the Incident or Problem that represents an associated service failure. This object is available in API version 53.0 and later.
  CaseShare
  Represents a sharing entry on a Case.
  CaseSolution
  Represents the association between a Case and a Solution.
  CaseStatus
  Represents the status of a Case, such as New, On Hold, or In Process.
  CaseSubjectParticle
  Represents the Social Business Rules custom format for the Case Subject field on cases created from inbound social posts. This object is available in API version 41.0 and later.
  CaseTag
  Associates a word or short phrase with a Case
  CaseTeamMember
  Represents a case team member, who works with a team of other users to help resolve a case.
  CaseTeamRole
  Represents a case team role. Every case team member has a role on a case, such as “Customer Contact” or “Case Manager.”
  CaseTeamTemplate
  Represents a predefined case team, which is a group of users that helps resolve a case.
  CaseTeamTemplateMember
  Represents a member on a predefined case team, which is a group of users that helps resolve cases.
  CaseTeamTemplateRecord
  The CaseTeamTemplateRecord object is a linking object between the Case and CaseTeamTemplate objects. To assign a predefined case team to a case (customer inquiry), create a CaseTeamTemplateRecord record and point the ParentId to the case and the TeamTemplateId to the predefined case team.
  CategoryData
  Represents a logical grouping of Solution records.
  CategoryNode
  Represents a tree of Solution categories.
  CategoryNodeLocalization
  When the Translation Workbench is enabled for your organization, the CategoryNodeLocalization object provides the translation of the label of a solution category.
  ChangeRequest
  Represents a decision to implement a formal request for a change (RFC). This object is available in API version 53.0 and later.
  ChangeRequestRelatedIssue
  Represents a junction object that relates a ChangeRequest to an Incident or Problem due to a service failure. This object is available in API version 53.0 and later.
  ChangeRequestRelatedItem
  Represents a junction object that relates a ChangeRequest to an Asset. This object is available in API version 53.0 and later.
  ChannelObjectLinkingRule
  Represents a rule for linking a channel interaction with an object (such as Lead or Contact). This object is available in API version 47.0 and later.
  ChannelProgram
  Represents a channel program that vendors use to market and sell their products through channel partners. This object is available in API version 41.0 and later.
  ChannelProgramLevel
  Represents a level, based on member experience, in a channel program. This object is available in API version 41.0 and later.
  ChannelProgramMember
  Represents a partner who is a member of a channel program. This object is available in API version 41.0 and later.
  ChatterActivity
  ChatterActivity represents the number of posts and comments made by a user and the number of comments and likes on posts and comments received by the same user. This object is available in API version 23.0 and later.
  ChatterAnswersActivity
  Represents the reputation of a User in Chatter Answers zones.This object is available in API version 25.0 and later.
  ChatterAnswersReputationLevel
  Represents a reputation level within a Chatter Answers zone. This object is available in API version 26.0 and later.
  ChatterConversation
  Represents a private conversation in Chatter, consisting of messages that conversation members have sent or received. This object is available in API version 23.0 and later.
  ChatterConversationMember
  Represents a member of a private conversation in Chatter. A member has either sent messages to or received messages from other conversation participants. This object is available in API version 23.0 and later.
  ChatterExtension
  Represents a Rich Publisher App that’s integrated with the Chatter publisher. This object is available in API version 41.0 and later.
  ChatterExtensionConfig
  Configuration for the Chatter extension for Experience Cloud sites. This object is available in API version 41.0 and later.
  ChatterMessage
  Represents a message sent as part of a private conversation in Chatter. This object is available in API version 23.0 and later.
  ClientBrowser
  Represents a cookie added to the browser upon login, and also includes information about the browser application where the cookie was inserted. This object is available in version 28.0 and later.
  CollaborationGroup
  Represents a Chatter group. This object is available in API version 19.0 and later.
  CollaborationGroupMember
  Represents a member of a Chatter group. This object is available in API version 19.0 and later.
  CollaborationGroupMemberRequest
  Represents a request to join a private Chatter group. This object is available in API version 21.0 and later.
  CollaborationGroupRecord
  Represents the records associated with Chatter groups.
  CollaborationInvitation
  Represents an invitation to join Chatter, either directly or through a group. This object is available in API version 21.0 and later.
  CollaborationRoom
  Represents a collaboration room, which links Salesforce to a Slack channel used by applications with specific use cases, such as swarming or reporting. This object is available in API version 55.0 and later.
  CollabDocumentMetric
  Represents the engagement metrics for a Quip thread (document or spreadsheet) that’s linked to a Salesforce record. This object is available in API version 50.0 and later.
  CollabDocumentMetricRecord
  Represents an association between a CollabDocumentMetric and a Salesforce record.It tracks which Salesforce record, such as an Account or Contact, is linked to a Quip thread for which metrics were gathered using CollabDocumentMetric. CollabDocumentMetricRecord is available in API version 50.0 and later.
  CollabTemplateMetric
  Represents the engagement metrics for a Quip template.This object is available in API version 50.0 and later.
  CollabTemplateMetricRecord
  Represents an association between a CollabTemplateMetric and a Salesforce record.It tracks which Salesforce record, such as an Account or Contact, is linked to a Quip template for which metrics were gathered using CollabTemplateMetric. CollabTemplateMetricRecord is available in API version 50.0 and later.
  CollabUserEngagementMetric
  Represents the user engagement metrics for a Quip thread in a Quip template or document. This object is available in API version 50.0 and later.
  CollabUserEngmtRecordLink
  Represents an association between a CollabUserEngagementMetric and a Salesforce record. It tracks which Salesforce record, such as an Account or Contact, is associated with the user engagement metric. This object is available in API version 50.0 and later.
  ColorDefinition
  Represents the color-related metadata for a custom tab. This object is available in API version 43.0 and later.
  CombinedAttachment
  This read-only object contains all notes, attachments, Google Docs, documents uploaded to libraries in Salesforce CRM Content, and files added to Chatter that are associated with a record.
  CommerceEntitlementBuyerGroup
  Represents the entitlement policy for a buyer group. This object is available in API version 49.0 and later.
  CommerceEntitlementPolicy
  Represents an entitlement policy, which determines what products and prices a user can see. This object is available in API version 49.0 and later.
  CommerceEntitlementPolicyShare
  Represents the entitlement rule for sharing products and prices with users other than the owner. This object is available in API version 49.0 and later.
  CommerceEntitlementProduct
  Represents the entitlement policy for a product. This object is available in API version 49.0 and later.
  CommissionSchedule
  Represents a commission calculation and rate definition. Calculates commission values for a commissionable event.
  CommissionScheduleAssignment
  Represents the commission calculation applicable to a specific product or producer for one or multiple commissionable events.
  CommSubscription
  Represents a customer’s subscription preferences for a specific communication. This object is available in API version 48.0 and later.
  CommSubscriptionChannelType
  Represents the engagement channel through which you can reach a customer for a communication subscription. This object is available in API version 48.0 and later.
  CommSubscriptionConsent
  Represents a customer’s consent to a communication subscription. This object is available in API version 48.0 and later.
  CommSubscriptionTiming
  Represents a customer's timing preferences for receiving a communication subscription. This object is available in API version 48.0 and later.
  Community (Zone)
  Represents a zone that contains Idea or Question objects.
  ConcurApexLimitEventLog
  Concurrent Apex Limit event logs contain information about long-running concurrent Apex requests in your org that Salesforce terminated after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted towards your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the long-running requests exceed the org default limit, additional long-running requests are denied. This object is available in API version 55.0 and later.
  ConnectedApplication
  Represents a connected app and its details; all fields are read-only.
  Consumption Rate
  Consumption rates describe the billing rate for a range of usage within a consumption schedule. All consumption schedules require at least one consumption rate in order to rate usage on a usage product. This object is available in API version 45.0 and later.
  Consumption Schedule
  A consumption schedule organizes a set of consumption rates by which usage-based products are quoted and billed. This object is available in API version 45.0 and later.
  Contact
  Represents a contact, which is a person associated with an account.
  ContactCenterChannel
  Represents a junction object that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a CallCenter object for Bring Your Own Channel for CCaaS. This object also represents the routing details for a voicemail configuration. This object is available in API version 56.0 and later.
  ContactCleanInfo
  Stores the metadata Data.com Clean uses to determine a contact record’s clean status. Helps you automate the cleaning or related processing of contact records. ContactCleanInfo includes a number of bit vector fields.
  ContactDailyMetric
  Represents the daily engagement metrics for a contact. This object is available in API version 52.0 and later.
  ContactMonthlyMetric
  Represents the monthly engagement metrics for a contact. This object is available in API version 52.0 and later.
  ContactPointAddress
  Represents a contact’s billing or shipping address, which is associated with an individual or person account. This object is available in API version 49.0 and later.
  ContactPointConsent
  Represents a customer's consent to be contacted via a specific contact point, such as an email address or phone number. This object is available in API version 48.0 and later.
  ContactPointEmail
  Represents a contact’s email, which is associated with an individual or person account. This object is available in API version 48.0 and later.
  ContactPointPhone
  Represents a contact’s phone number, which is associated with an individual or person account. This object is available in API version 48.0 and later.
  ContactPointTypeConsent
  Represents consent for a contact point type, such as email or phone. This object is available in API version 45.0 and later.
  ContactOwnerSharingRule
  Represents the rules for sharing a contact with a User other than the owner.
  ContactRequest
  Represents a customer’s request for support to get back to them about an issue. This object is available in API version 45.0 and later.
  ContactRequestShare
  Represents a list of access levels to a ContactRequest with an explanation of the access level. This object is available in API version 45.0 and later.
  ContactShare
  Represents a list of access levels to a Contact along with an explanation of the access level. For example, if you have access to a record because you own it, the ContactAccessLevel is All and RowCause is Owner.
  ContactSuggestionInsight
  Represents a suggestion for a new contact record. Available in API versions 45.0 and later.
  ContactTag
  Associates a word or short phrase with a Contact.
  ContentAsset
  Represents a Salesforce file that has been converted to an asset file in a custom app in Lightning Experience. Use asset files for org setup and configuration. Asset files can be packaged and referenced by other components. This object is available in API version 38.0 and later.
  ContentBody
  Represents the body of a file in Salesforce CRM Content or Salesforce Files. This object is available in API version 40.0 and later.
  ContentDistribution
  Represents information about sharing a document externally. This object is available in API version 32.0 and later.
  ContentDistributionView
  Represents information about views of a shared document. This read-only object is available in API version 32.0 and later.
  ContentDocument
  Represents a document that has been uploaded to a library in Salesforce CRM Content or Salesforce Files. This object is available in versions 17.0 and later for Salesforce CRM Content. This object is available in API version 21.0 and later for Salesforce Files.
  ContentDocumentHistory
  Represents the history of a document. This object is available in versions 17.0 and later.
  ContentDocumentLink
  Represents the link between a Salesforce CRM Content document, Salesforce file, or ContentNote and where it's shared. A file can be shared with other users, groups, records, and Salesforce CRM Content libraries. This object is available in versions 21.0 and later for Salesforce CRM Content documents and Salesforce Files.
  ContentDocumentListViewMapping
  Represents an association between a ListView and a Quip ContentDocument. Applies to Quip file types only. Maintains the mapping between a list view and Quip document when the list view is exported to a newly created Quip document. This object is available in API version 44.0 and later.
  ContentDocumentSubscription
  Represents a subscription for a user following or commenting on a file in a library. This object is available in API version 42.0 and later.
  ContentFolder
  Represents a folder in a content library for adding files. This object is available in API version 34.0 and later.
  ContentFolderItem
  Represents a file (ContentDocument) or folder (ContentFolder) that resides in a ContentFolder in a ContentWorkspace. This object is available in API version 35.0 and later.
  ContentFolderLink
  Defines the association between a library and its root folder. This object is available in API version 34.0 and later.
  ContentFolderMember
  Defines the association between a file and a folder. This object is available in API version 34.0 and later.
  ContentHubItem
  Represents a file or folder in a Files Connect external data source, such as Microsoft SharePoint or OneDrive for Business. This object is available in API version 33.0 and later.
  ContentHubRepository
  Represents a Files Connect external data source such as Microsoft SharePoint or OneDrive for Business. This object is available in API version 33.0 and later.
  ContentNote
  Represents a note created with the enhanced note taking tool, released in Winter ‘16. This object is available in API version 32.0 and later.
  ContentNotification
  Represents a notification for a file. This object is available in API version 42.0 and later.
  ContentTagSubscription
  Represents a subscription for a user following a tag on a file. This object is available in API version 42.0 and later.
  ContentTaxonomy
  Represents a content taxonomy, which is used to classify and organize Salesforce CMS content. To create a hierarchy of terms in a content taxonomy, use this object in addition to the ContentTaxonomyTerm, ContentTaxonomyRelatedTerm, and ContentTaxonomyTermRelatedTerm objects. This object is available in API version 63.0 and later.
  ContentTaxonomyRelatedTerm
  Represents the relationship between a term and the content taxonomy to which the term belongs. This object is available in API version 63.0 and later.
  ContentTaxonomyTerm
  Represents a term in a content taxonomy. Terms describe what content is or how it's used, and they’re organized in parent-child relationships in the taxonomy hierarchy. This object is available in API version 63.0 and later.
  ContentTaxonomyTermRelatedTerm
  Represents the relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.
  ContentTaxonomyTermRelationshipType
  Represents the type of relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.
  ContentTransferEventLog
  ContentTransferEventLog stores information about content transfer events, such as downloads, uploads, and previews. This information includes events performed on files and attachments to records. This object is available in API version 62.0 and later.
  ContentUserSubscription
  Represents a subscription for a user following another user. This object is available in API version 42.0 and later.
  ContentVersion
  Represents a specific version of a document in Salesforce CRM Content or Salesforce Files. This object is available in versions 17.0 and later for Salesforce CRM Content documents. This object is available in versions 20.0 and later for Salesforce Files.
  ContentVersionComment
  Represents a comment on a version of a file. This object is available in API version 42.0 and later.
  ContentVersionHistory
  Represents the history of a specific version of a document. This object is available in version 17.0 and later.
  ContentVersionRating
  Represents a rating on a version of a file. This object is available in API version 42.0 and later.
  ContentWorkspace
  Represents a content library. This object is available in versions 17.0 and later.
  ContentWorkspaceDoc
  Represents a link between a document and a public library in Salesforce CRM Content. This object is available in versions 17.0 and later.
  ContentWorkspaceMember
  Represents a member of a content library. This object is available in API version 40.0 and later.
  ContentWorkspacePermission
  Represents a library permission. This object is available in API version 40.0 and later.
  ContentWorkspaceSubscription
  Represents a subscription for a user following a library. This object is available in API version 42.0 and later.
  ContextParamMap
  Represents optional context data for a Conversation or a ConversationParticipant. This object is available in API version 57.0 and later.
  Contract
  Represents a contract (a business agreement) associated with an Account.
  ContractContactRole
  Represents the role that a Contact plays on a Contract.
  ContractLineItem
  Represents a product covered by a service contract (customer support agreement). This object is available in API version 18.0 and later.
  ContractLineOutcome
  Represents information on a contract line outcome’s captured data and other related parameters that are used when capturing data. This object is available in API version 58.0 and later.
  ContractLineOutcomeData
  Represents the contract line outcome’s captured data. It stores the data that was captured between the contract line outcome’s start date and end date. This object is available in API version 58.0 and later.
  ContractStatus
  Represents the status of a Contract, such as Draft, InApproval, Activated, Terminated, or Expired.
  ContractTag
  Associates a word or short phrase with a Contract.
  Conversation
  Represents a conversation between an end user and an agent. Available in API version 49.0 and later.
  ConversationContextEntry
  Represents the context of a message or an event in the chat history between an agent and a messaging user. This object is available in API version 47.0 and later.
  ConversationChannelDefinition
  Represents a configurable definition of a conversation channel that’s implemented for Interaction Service for Bring Your Own Channel and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.
  ConversationEntry
  Represents a message or event in a voice call or a standard or enhanced messaging session. This object is available in API version 43.0 and later.
  ConversationParticipant
  Represents an active participant in a conversation. A new ConversationParticipant record is created each time a participant joins a conversation. This object is available in API version 49.0 and later.
  ConvMessageSendRequest
  Represents a request to send a template-based messaging component to a series of messaging users in an enhanced WhatsApp, enhanced Apple Messages for Business, or Messaging for In-App and Web channel. This object is available in API version 60.0 and later.
  ConversationVendorInfo
  This setup object connects the partner vendor system to the Service Cloud feature. For example, for Service Cloud Voice, this object contains information about the partner telephony or Contact Center as a Service (CCaaS) partner system. For Bring Your Own Channel this object contains information about the partner messaging system, and for Bring Your Own Channel for CCaaS, this object contains information about the CCaaS partner system. This object is available in API version 52.0 and later.
  CorsWhitelistEntry
  Represents an entry in the cross-origin resource sharing (CORS) allowlist. Origins included in the allowlist can request REST resources from that Salesforce org.
  Coupon
  A coupon associated with a promotion. This object is available in API version 54.0 and later.
  CouponCodeRedemption
  Tracks each coupon code redemption. This object is available in API version 58.0 and later.
  CreditMemo
  Represents a document that is used to reduce the amount that a buyer owes a seller under the terms of an earlier invoice. This object is available in API version 48.0 and later.
  CreditMemoAddressGroup
  Stores the buyer's address information, which is used to determine the amount of tax to credit to a buyer when a credit memo is issued. This object is available in API version 55.0 and later.
  CreditMemoInvApplication
  Represents an amount applied from a credit memo to an invoice. This object is available in API version 48.0 and later.
  CreditMemoLine
  Represents product, service, adjustment, or tax line items that were included in a credit memo. This object is available in API version 48.0 and later.
  Crisis
  Represents a major crisis event that affects an Employee in an InternalOrganizationUnit. This object is available in API version 48.0 and later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.
  CronJobDetail
  Contains details about the associated scheduled job, such as the job’s name and type. This object is available in API version 29.0 and later.
  CronTrigger
  Contains schedule information for a scheduled job. CronTrigger is similar to a cron job on UNIX systems. This object is available in API version 17.0 and later.
  CryptoProdCatgWalletGroup
  Specifies if CryptoWalletGroup is in the allowlist or airdrop for the ProductCategory. A custom object between ProductCategory and CryptoWalletGroup adding the CryptoWalletGroup to allowlist or airdrop. This object is available in API version 58.0 and later.
  CspTrustedSite
  Represents a trusted URL. For each CspTrustedSite, you can specify Content Security Policy (CSP) directives and permissions policy directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource type from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL access to a browser feature. In API version 58.0 and earlier, CspTrustedSite included only CSP directives and was referred to as CSP Trusted Sites in Salesforce Setup. Available in API version 39.0 and later.
  CurrencyType
  Represents the currencies used by an organization for which the multicurrency feature is enabled.
  CustomBrand
  Represents a custom branding and color scheme. This object is available in API version 28.0 and later.
  CustomBrandAsset
  Represents a branding element in a custom branding scheme. For example, a color, logo image, header image, or footer text. A CustomBrandAsset can apply to an Experience Cloud site or to an org using the Salesforce mobile app. This object is available in API version 28.0 and later.
  CustomFieldDisplayValue
  Stores variation details for the product attribute item view. This object is available in API version 63.0 and later.
  CustomHelpMenuItem
  Represents the items within a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources. This object is available in API version 44.0 and later.
  CustomHelpMenuSection
  Represents a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources. This object is available in API version 44.0 and later.
  CustomHttpHeader
  Represents a custom HTTP header that provides context information from Salesforce such as region, org details, or the role of the person viewing the external object. This object is available in API version 43.0 and later.
  CustomMsgChannel
  Represents a custom conversation channel and stores event-driven Messaging settings. Custom conversation channels are implemented for Bring Your Own Channel and Bring Your Own Channel for CCaaS Messaging channels. This object is available in API version 63.0 and later.
  CustomNotificationType
  Stores information about custom notification types. This object is available in API version 47.0 and later.
  CustomPermission
  Represents a permission created to control access to a custom process or app, such as sending email. This object is available in API version 31.0 and later.
  CustomPermissionDependency
  Represents the dependency between two custom permissions when one custom permission requires that you enable another custom permission. This object is available in API version 32.0 and later.
  Customer
  Represents the customer role of an individual with respect to a particular company or organization. This object is available in API version 53.0 and later.
  DandBCompany
  Represents a Dun & Bradstreet® company record, which is associated with an account added from Data.com. This object is available in API version 25.0 and later.
  Dashboard
  Represents a dashboard, which shows data from custom reports as visual components. Access is read-only. This object is available in API version 20.0 and later.
  DashboardComponent
  Represents a dashboard component, which can be a chart, metric, table, or gauge on a dashboard. Access is read-only. This object is available in API version 21.0 and later.
  DashboardTag
  Associates a word or short phrase with a Dashboard. This object is available in API version 20.0 and later.
  DataAssessmentFieldMetric
  Represents summary statistics for matched, blank, and differing fields in account records of an org compared to records in Data.com. This object is available in API version 37.0 and later.
  DataAssessmentMetric
  Represents a summary of statistics for fields matched and unmatched in your account records with Data.com account records. This object is available in API version 37.0 and later.
  DataAssessmentValueMetric
  Summarizes the number of fields matched for your account records with Data.com account records.This object is available in API version 37.0 and later.
  DatacloudCompany
  Represents the fields for Data.com company records. This object is available in API version 30.0 or later.
  DatacloudContact
  The fields and properties for Data.com contact records. This object is available in API version 30.0 or later.
  DatacloudDandBCompany
  Represents a set of read-only fields that are used to return D&B company data from Data.com API calls. This object is available in API version 30.0 or later.
  DatacloudOwnedEntity
  Represents fields in the DatacloudOwnedEntity object. The DatacloudOwnedEntity object tracks user-purchased records. This object is available in API version 30.0 or later.
  DatacloudPurchaseUsage
  Represents an object used to identify and track Data.com record purchases. This object is available in API version 30.0 or later.
  DataEncryptionKey
  The DataEncryptionKey object is part of the Bring Your Own Key (BYOK) feature, which allows users to upload a data encryption key (DEK) using a public key generated by the Salesforce Shield Key Management Service (KMS). Customers create their own DEKs and upload them to Salesforce. Users access this entity via the API to list DEK keys for auditing purposes. They can also programmatically upload key material. This object is available in API version 63.0 and later.
  DataIntegrationRecordPurchasePermission
  Indicates Lightning Data purchase credits that a Salesforce admin has granted to users.
  DataKitDeployEvent
  Represents a data kit deployment event that notifies subscribers of the status of the data kit component deployment. This object is available in API version 61.0 or later.
  DataKitDeploymentLog
  Represents the log details of a data kit component deployment. This object is available in API version 61.0 or later.
  DatasetExport
  Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExport acts as the header and includes the JSON schema.
  DatasetExportPart
  Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExportPart contains parts of the .csv file.
  DataMaskCustomValueLibrary
  Represents a set of user-inputted values in a custom library in Data Mask. This object is available in API version 63.0 and later.
  DataStatistics
  For internal use only.
  DataUseLegalBasis
  Represents the legal basis for contacting a customer, such as billing or contract. This object is available in API version 45.0 and later.
  DataUsePurpose
  Represents the reason for contacting a prospect or customer, such as for billing, marketing, or surveys. This object is available in API version 45.0 and later.
  DataWeaveResource
  Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. This object is available in API version 58.0 and later.
  DatedConversionRate
  Represents the dated exchange rates used by an organization for which the multicurrency and the effective dated currency features are enabled.
  DeclinedEventRelation
  Represents event participants (invitees or attendees) with the status Declined for a given event. This object is available in API versions 29.0 and later.
  DelegatedAccount
  Represents the external managed account. This object is available in API version 49.0 and later.
  DeleteEvent
  Represents a record that has been soft deleted. Search on this object was available in API version 48.0, then removed in API version 50.0.
  DeliveryEstimationSetup
  Shows the configuration options for the commerce delivery service offered through a web store or sales channel. Includes settings such as delivery location group, channel, fulfillment types, and default fulfillment time. This object is available in API version 61.0 and later.
  DigitalSignature
  Represents a signature captured on a service report in field service.
  DigitalWallet
  Represents a customer’s digital wallet service. Salesforce Payments can use a digital wallet as a payment source when processing payments through a payment gateway. This object is available in API version 48.0 and later.
  DirectMessage
  Represents a direct message conversation between multiple users in Chatter. This object is available in API version 38.0 and later.
  Division
  A logical segment of your organization's data. For example, if your company is organized into different business units, you could create a division for each business unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division permission enabled.
  DivisionLocalization
  When the Translation Workbench is enabled for your organization, the DivisionLocalization object provides the translation of the label for a division.
  Document
  Represents a file that a user has uploaded. Unlike Attachment records, documents are not attached to a parent object.
  DocumentAttachmentMap
  Maps the relationship between an EmailTemplate and its attachment, which is stored as a Document.
  DocumentRecipient
  Connects a Service Report to a Digital Signature. This object is available in API version 55.0 and later.
  DocumentTag
  Associates a word or short phrase with a Document.
  Domain
  Read-only object that represents a custom Web address assigned to a site in your organization. This object is available in API version 26.0 and later.
  DomainSite
  Read-only junction object that joins the Site and Domain objects. This object is available in API version 26.0 and later.
  DsarPolicy
  Represents a Data Subject Access Request (DSAR) policy created in the Privacy Center managed package. DSAR policies anonymize or transfer personal data from your org at your customer’s request. This object is available in API version 50.0 and later.
  DsarPolicyLog
  Represents the history of Data Subject Access Request (DSAR) policy execution requests. This log records the status and results of executed DSAR policies for a customer. This object is available in API version 50.0 and later.
  DuplicateJob
  Represents an instance of a job that identifies duplicates among existing records in the system.
  DuplicateJobDefinition
  Setup object defining a job that identifies duplicate record items globally.
  DuplicateJobMatchingRule
  Represents a MatchingRule to be used with a DuplicateJob sharing the corresponding DuplicateJobMatchingRuleDefinition.
  DuplicateJobMatchingRuleDefinition
  Setup object specifying a MatchingRule to use with DuplicateJob instances that share a DuplicateJobDefinition.
  DuplicateRecordItem
  Represents an individual record that’s part of a duplicate record set. Use this object to create custom report types.
  DuplicateRecordSet
  Represents a group of records that have been identified as duplicates. Each duplicate record set contains one or more duplicate record items. Use this object to create custom report types and view the results of duplicate jobs.
  DuplicateRule
  Represents a duplicate rule for detecting duplicate records.
  ElectronicMediaGroup
  Represents the type of media that you can associate with a product or category.This object is available in API version 49.0 and later.
  ElectronicMediaUse
  Represents the usage of media. This object is available in API version 49.0 and later.
  EmailContent
  Represents a marketing email asset for use with Account Engagement. This object is available in API version 50.0 and later.
  EmailDomainFilter
  Represents a filter that determines whether an email relay is restricted to a specific list of domains. This object is available in API version 43.0 and later.
  EmailDomainKey
  Represents a domain key for an organization’s domain, used to authenticate outbound email that Salesforce sends on the organization’s behalf. This object is available in API version 28.0 and later.
  EmailMessage
  Represents an email in Salesforce.
  EmailMessageRelation
  Represents the relationship between an email and contacts, leads, and users. This object is available in API version 37.0 and later.
  EmailRelay
  Represents the configuration for sending an email relay. An email relay routes email sent from Salesforce through your company’s email servers. This object is available in API version 43.0 and later.
  EmailRoutingAddress
  An email address used for Email-to-Case. Email routing addresses store a unique email services address provided by Salesforce and configuration options for emails received by this address.
  EmailServicesAddress
  An email service address.
  EmailServicesFunction
  An email service.
  EmailStatus
  Represents the status of email sent.
  EmailTemplate
  Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed packages only.
  EmailTemplateMonthlyMetric
  Represents the monthly engagement metrics for an email template. This object is available in API version 53.0 and later.
  EmbeddedServiceDetail
  Represents a metadata catalog object that exposes fields from the underlying Embedded Service setup objects defined in each EmbeddedServiceConfig deployment for guest users. Guest users don’t have direct access to the Embedded Service setup objects. Available in API version 39.0 and later.
  EmbeddedServiceLabel
  Represents a customized label in Embedded Chat or embedded Appointment Management.This object is available in API version 44.0 and later.
  Employee
  Represents an employee within a company or organization. This object is available in API version 48.0 and later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.
  Employee2
  Represents an employee within a company or an organization. This object is available in API version 62.0 and later.
  EmployeeCrisisAssessment
  Represents a crisis assessment of an Employee. This object is available in API version 48.0 and later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.
  EmpUserProvisioningProcess
  Represents an employee-user provisioning process. This object is available in API version 52.0 and later.
  EmpUserProvisionProcessErr
  Represents an employee-user provisioning process error. This object is available in API version 52.0 and later.
  EnablementMeasureDefinition
  Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic, for tracking the activity. This object also represents Enablement measure information in Metadata API. This object is available in API version 56.0 and later.
  EnablementProgram
  Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific outcomes related to your company’s revenue goals. This object is available in API version 56.0 and later.
  EnablementProgramDefinition
  Represents Enablement program information in Metadata API. This object is available in API version 61.0 and later.
  EnblMeasureObjectDefinition
  Represents the criteria for an object that tracks the job-related activity for an Enablement measure in an Enablement program. A separate EnblMeasureObjectDefinition is used for a measure's source object and each optional related object. This object is available in API version 56.0 and later.
  EnblPgmTaskMeasureProgress
  Represents a user’s progress through the object and field requirements that an Enablement measure defines for an outcome or milestone in an Enablement program. This object is available in API version 61.0 and later.
  EnblProgramSection
  Represents an optional section in an Enablement program. A section can include other program items, such as milestones and exercises. This object is available in API version 60.0 and later.
  EnblProgramTaskDefinition
  Represents an outcome, a milestone, or an exercise in an Enablement program. A program task is also known as a program item. This object is available in API version 60.0 and later.
  EnblProgramTaskMeasure
  Represents the connection between an Enablement measure and a specific milestone or outcome in an Enablement program. This object is available in API version 61.0 and later.
  EnblProgramTaskProgress
  Represents a user’s progress towards completing an outcome, a milestone, or an exercise in an Enablement program. This object is available in API version 60.0 and later.
  EnblProgramTaskSubCategory
  Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and LearningItemType records for when users take the exercise in the Guidance Center. This object is available in API version 62.0 and later.
  EngagementChannelType
  Represents a channel through which a customer can be reached for communication. This object is available in API version 48.0 and later.
  EnhancedLetterhead
  Represents an enhanced letterhead that can be associated with a Lightning email template that doesn’t use the Salesforce Merge Language (SML). This object is available in API version 46.0 and later.
  Entitlement
  Represents the customer support an account or contact is eligible to receive. This object is available in API version 18.0 and later. Entitlements may be based on an asset, product, or service contract.
  EntitlementContact
  Represents a Contact eligible to receive customer support via an Entitlement. This object is available in API version 18.0 and later.
  EntitlementTemplate
  Represents predefined terms of customer support for a product (Product2). This object is available in API version 18.0 and later.
  EntityHistory
  Represents historical information about an object’s changed field values. This object is only available to users with the “View All Data” permission. This object is unavailable beginning with API version 8.0. Use the object-specific Historyobjects instead.
  EntityMilestone
  Represents a required step in a customer support process on a work order. The Salesforce user interface uses the term “object milestone. This object is available in API version 37.0 and later.
  EntitySubscription
  Represents a subscription for a user following a record or another user. This object is available in API version 34.0 and later.
  EnvironmentHubMember
  Represents a member organization in the Environment Hub. This object is available in API version 29.0 and later.
  Event
  Represents an event in the calendar. In the user interface, event and task records are collectively referred to as activities.
  EventLogFile
  Represents event log files for event monitoring. The event monitoring product gathers information about your Salesforce org’s operational events, which you can use to analyze usage trends and user behavior. This object is available in API version 32.0 and later. The Interval and Sequence fields are available only in API version 37.0 and later.
  EventRelation
  Represents a person (a user, lead, or contact) or a resource (such as a conference room) invited to an event. This object lets you add or remove invitees from an event and use the API to manage invitees’ responses to invitations. If Shared Activities is enabled, EventRelation can also represent other objects that are related to an event. EventRelation does not support triggers, workflow, or data validation rules.
  EventBusSubscriber
  Represents a trigger, process, or flow that’s subscribed to a platform event or a change data capture event. Doesn’t include CometD or Pub/Sub API subscribers.
  EventRelayConfig
  Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to Amazon EventBridge. This object is available in API version 56.0 and later.
  EventRelayFeedback
  Represents execution state information about an event relay from Salesforce to Amazon EventBridge for platform events and change data capture events. Query this object to get information such as the event relay status and any error message. This object is available in API version 56.0 and later.
  EventTag
  Associates a word or short phrase with an Event.
  EventWhoRelation
  Represents the relationship between an event and a lead or contacts. This derived object is a filtered version of the EventRelation object; that is, IsParent is true and IsWhat is false. It doesn’t represent relationships to invitees or to accounts, opportunities, or other objects. This object is available in API versions 29.0 and later.
  Expense
  Represents an expense linked to a work order. Service resource technicians can log expenses, such as tools or travel costs. This object is available in API version 49.0 and later.
  ExpenseReport
  Represents a report that summarizes expenses. This object is available in API version 50.0 and later.
  ExpenseReportEntry
  Represents an entry in an expense report. This object is available in API version 50.0 and later.
  ExpressionFilter
  Represents a logical expression that’s used to control the execution of macro instructions. This object is available in API version 46.0 and later.
  ExpressionFilterCriteria
  Represents a condition in an expression that’s used to control the execution of macro instructions. This object is available in API version 46.0 and later.
  ExternalAccountHierarchy
  Represents the external account hierarchy, which works like a role-based hierarchy. Use ExternalAccountHierarchy to allow partner and customer users to share data with other external accounts in their hierarchy.This object is available in API version 49.0 and later.
  ExternalAccountHierarchyHistory
  Represents the history of changes to values in the fields of an external account hierarchy. This object is available in API version 50.0 and later.
  ExternalClientApplication
  For internal use only.
  ExternalDataSource
  Represents an external data source, which defines connection details for integration with data and content that are stored outside the Salesforce org. This object is available in API version 27.0 and later.
  ExternalDataUserAuth
  Stores authentication settings for a Salesforce user to access an external system. The external system must be defined in an external data source or a named credential that’s configured to use per-user authentication. This object is available in API version 27.0 and later.
  ExternalEncryptionRootKey
  Represents metadata about root keys stored in third-party key stores that are used to generate and secure keys that encrypt Salesforce data. This object is available in API version 58.0 and later.
  ExternalSocialAccount
  Represents a managed social media account on a social network such as Facebook or Twitter. This object is available in API version 29.0 and later.
  ExtKnowledgeConnector
  Represents a connector to a third-party knowledge source for Unified Knowledge. This object is available in API version 60.0 and later.
  ExtlClntAppOauthPlcyCnfg
  For internal use only.
  ExtlClntAppOauthSettings
  For internal use only.
  ExtlClntAppPlcyCnfg
  For internal use only.
  ExtlRecShrCnct
  Represents authentication data to make outbound calls to and inbound calls from an external system to publish events for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrCnctAccnt
  Represents an association between an account and an external record share connection for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrField
  Represents an imported, exported, or updated external record share field for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrFieldMap
  Represents the external record share field mapping between the sender and receiver for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrLead
  Represents the Lead record of a vendor org if you’re a partner. If you’re a vendor for Partner Connect, this object represents a partner org. This object is available in API version 62.0 and later.
  ExtlRecShrObject
  Represents a shared object for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrOpportunity
  Represents the opportunity for Partner Connect in the vendor org if you’re a partner and the partner org if you’re the vendor. This object is available in API version 62.0 and later.
  ExtlRecShrPcklstOptn
  Represents a picklist option of an external record share picklist field shared between a partner and vendor for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrPicklistMap
  Represents the external record share picklist field mapping between the partner and vendor system for Partner Connect. This object is available in API version 62.0 and later.
  ExtlRecShrRecordMap
  Represents the lead or opportunity being mapped between a partner and vendor for Partner Connect. This object is available in API version 62.0 and later.
  FeedAttachment
  Represents an attachment to a feed item, such as a file attachment or a link. Use FeedAttachment to add various attachments to one feed item. This object is available in API version 36.0 and later.
  FeedComment
  Represents a comment added to a feed by a user. This object is available in API version 18.0 and later.
  FeedItem
  FeedItem represents an entry in the feed, such as changes in a record feed, including text posts, link posts, and content posts. This object is available in API version 21.0 and later. This object replaces FeedPost.
  FeedLike
  Indicates that a user has liked a feed item. This object is available in API version 21.0 and later.
  FeedPollChoice
  Shows the choices for a poll posted in the feed. This object is available in API version 29.0 and later.
  FeedPollVote
  Shows how users voted on a poll posted in the feed. This object is available in API version 29.0 and later.
  FeedPost
  FeedPost represents the following types of changes in a record feed, such as AccountFeed: text posts, link posts, and content posts. This object is available in API version 18.0 through 21.0. FeedPost is no longer available in later versions. Starting with API version 21.0, use FeedItem to represent text posts, link posts, and content posts in feeds.
  FeedRevision
  Holds the revision history of a specific feed item or comment, including a list of attributes that changed for each revision. This object is available in API version 34.0 and later.
  feedSignal
  Attach feed signals, like UpDownVote, UserVerified, and Verified, to a feed post or comment. This object is available in API version 41.0 and later.
  FeedTrackedChange
  Represents an individual field change or set of field changes. A FeedTrackedChange is a child object of a record feed, such as AccountFeed. This object is available in API version 18.0 and later.
  FieldHistoryArchive
  Represents field history values for all objects that retain field history. FieldHistoryArchive is a big object, available only to users with the “Retain Field History” permission. This object is available in API version 29.0 and later.
  FieldChangeSnapshot
  Use this virtual object to learn which opportunities' close dates changed during the specified time period. This object is available in API version 52.0 and later.
  FieldPermissions
  Represents the enabled field permissions for the parent PermissionSet. This object is available in API version 24.0 and later.
  FieldSecurityClassification
  Represents a field’s data sensitivity value selected from the SecurityClassification picklist. This object is available in API version 46.0 and later.
  FieldServiceMobileSettings
  Represents a configuration of settings that control the Field Service iOS and Android mobile app experience. This object is available in API version 38.0 and later.
  FieldServiceOrgSettings
  Represents the org settings for Field Service, such as Appointment Assistant settings. If Field Service is enabled, the org contains one read-only record of this object. This object is available in API version 51.0 and later.
  FileSearchActivity
  Represents search activity on a file. This object is available in API version 38.0 and later.
  FiscalYearSettings
  Settings to define a custom or standard fiscal year for your organization. This object has a parent-child relationship with the Period object.
  FlexQueueItem
  Represents an asynchronous Apex job in the Apex flex queue. Provides information about the job type and flex queue position of the AsyncApexJob. This object is available in API version 36.0 and later.
  FlowDefinitionView
  Represents the description of a flow definition. This object is available in API version 46.0 and later.
  FlowInterview
  Represents a flow interview. A flow interview is a running instance of a flow. This object is available in API version 32.0 and later.
  FlowInterviewLog
  Represents the logs of a screen flow interview. An interview is an instance of a running or previously run flow.This object is available in API version 49.0 and later.
  FlowInterviewLogEntry
  Represents the log of a specific element that’s executed by a screen flow interview. An interview is an instance of a running or previously run flow. This object is available in API version 49.0 and later.
  FlowInterviewLogOwnerSharingRule
  Represents the rules for sharing a FlowInterviewLog with users other than the owner.This object is available in API version 49.0 and later.
  FlowInterviewOwnerSharingRule
  Represents the rules for sharing a FlowInterview with users other than the owner. This object is available in API version 33.0 and later.
  FlowInterviewShare
  Represents a sharing entry on a FlowInterview. This object is available in API version 33.0 and later.
  FlowNavMetricEventLog
  Flow Navigation Metric event logs contain metric data for flow interviews such as total execution time, number of interviews, and number of errors. This object is available in API version 55.0 and later.
  FlowOrchestration
  Represents the details of an orchestration definition. This object is available in API version 62.0 and later.
  FlowOrchestrationInstance
  Represents a run-time instance of an orchestration. This object is available in API version 53.0 and later.
  FlowOrchestrationLog
  Represents logging data for a FlowOrchestrationInstance. This object is available in API version 54.0 and later.
  FlowOrchestrationStageInstance
  Represents a run-time instance of a stage in a run-time instance of an orchestration. This read-only object is available in API version 53.0 and later.
  FlowOrchestrationStepInstance
  Represents a run-time instance of a step in a run-time instance of a stage of a run-time instance of an orchestration. This read-only object is available in API version 53.0 and later.
  FlowOrchestrationVersion
  Represents the version of an orchestration. This object is available in API version 62.0 and later.
  FlowOrchestrationWorkItem
  Represents a work item associated with a run-time instance of an interactive step in a run-time instance of an orchestration. This object is available in API version 54.0 and later.
  FlowRecord
  Represents the details of a flow. This object is available in API version 58.0 and later.
  FlowRecordElement
  Represents a single element within a flow version. This object is available in API version 58.0 and later.
  FlowRecordElementOccurrence
  Represents the execution metrics for a single element within a flow version. This object is available in API version 62.0 and later.
  FlowRecordRelation
  Represents a relationship between a record and a flow interview. When a flow interview is paused, Salesforce uses the $Flow.CurrentRecord global variable in the flow to associate the interview with a record. Available in API version 42.0 and later.
  FlowRecordVersion
  Represents the version of a flow. This object is available in API version 58.0 and later.
  FlowRecordVersionOccurrence
  Represents an instance of a recurring flow that runs on a schedule. For example, a flow that runs weekly on Wednesdays creates an occurrence each time it runs. This object is available in API version 60.0 and later.
  FlowTestResult
  Represents the results for a flow test associated with a flow version. This object is available in API version 55.0 and later.
  FlowTestView
  Represents the description of a flow test associated with a flow definition. This object is available in API version 55.0 and later.
  FlowStageRelation
  Represents a relationship between a paused flow interview and its stages. When a flow interview is paused, Salesforce creates a FlowStageRelation record for each stage that’s set to the $Flow.CurrentStage or $Flow.ActiveStages global variable. Available in API version 43.0 and later.
  FlowVariableView
  Represents a variable within the flow version. This object is available in API version 46.0 and later.
  FlowVersionView
  Represents the version of a flow definition. This object is available in API version 46.0 and later.
  Folder
  Represents a repository for a Dashboard, Document, EmailTemplate, Macro, QuickText, or Report. Only one type of item can be contained in a folder.
  FolderedContentDocument
  Represents the relationship between a parent and child ContentFolderItem in a ContentWorkspace.
  ForecastingAdjustment
  This object represents an individual forecast manager’s adjustment for a subordinate’s or child territory’s forecast via a ForecastingItem. Available in API versions 26.0 and later. This object is different from the ForecastingOwnerAdjustment object, which represents forecast users’ adjustments of their own forecasts, including territory forecasts they own.
  ForecastingColumnDefinition
  Represents a custom calculated column or a custom reference data column in a forecast type. This object is available in API version 56.0 and later.
  ForecastingColumnDefinitionLocalization
  Represents the translated value of a custom calculated column or custom reference data column label when the Translation Workbench is enabled for your organization. This object is available in API version 56.0 and later.
  ForecastingCustomCategory
  Represents a custom forecasting category used for forecast rollups. This object is available in API version 62.0 and later.
  ForecastingCustomData
  Represents forecast data from external sources to display in the forecasts page. For example, risk or last year’s revenue. This object is available in API version 58.0 and later.
  ForecastingDisplayedFamily
  Represents the table in Forecasts Settings where an admin selects the product families that users can forecast on in Lightning Experience. This object is available in API version 40.0 and later.
  ForecastingFact
  This object is read-only and links a ForecastingItem with its opportunities, such as opportunities that share the same owner or forecast category and have a closing date within the period of the forecasting item. Available in API versions 26 and greater.
  ForecastingFilter
  Represents the custom filter for including or excluding data from opportunity forecasts. This object is available in API version 54.0 and later.
  ForecastingFilterCondition
  Represents the custom filter condition logic for including or excluding data from opportunity forecasts. This object is available in API version 54.0 and later.
  ForecastingGroup
  Represents groups used to roll up forecast totals on the forecasts page. For example, group forecasts by industry or sales type. This object is available in API version 60.0 and later.
  ForecastingGroupItem
  Represents the value within the picklist that is specified as the forecasting group for a forecast type. For example, if you have a forecasting group that identifies the industry an opportunity is part of, this object represents the value in the the industry picklist that’s chosen to be part of the group. This object is available in API version 60.0 and later.
  ForecastingItem
  This object is read-only used for individual forecast amounts. Users see amounts based on their perspectives and forecast roles. The amounts users see include one of these values when forecasting in revenue: AmountWithoutAdjustments, AmountWithoutManagerAdjustment, ForecastAmount, OwnerOnlyAmount. The amounts users see include one of these values when forecasting in quantity: QuantityWithoutAdjustments, QuantityWithoutManagerAdjustment, ForecastQuantity, OwnerOnlyQuantity. Available in API version 26.0 and later.
  ForecastingOwnerAdjustment
  This object represents an individual forecast user’s adjustment of their own forecast, including territory forecasts they own, via a ForecastingItem. Available in API versions 33.0 and later. This object is different from the ForecastingAdjustment object, which represents managers’ adjustments of subordinates’ and child territories’ forecasts.
  ForecastingQuota
  This object represents an individual user’s or territory’s quota for a specified time period. The Managed Quotas user permission is required for creating, updating, or deleting quotas. (Users can only edit their subordinates’ or child territories’ quotas, not their own.) The View All Forecasts permission is required to view any user's forecast, regardless of the forecast hierarchy. Available in API versions 25.0 and later. Forecast managers can view the forecasts of subordinates and territories below them in the forecast hierarchy.
  ForecastingShare
  Represents forecasts shared between a forecast manager and a user. Available in API version 44.0 and later.
  ForecastingSourceDefinition
  Represents the object, measure, date type, and hierarchy that a forecast uses to project sales. This object is available in API version 52.0 and later.
  ForecastingSrcRecJudgment
  Represents forecast managers’ judgment of whether they consider an opportunity-related deal to be certain to close. This object is available in API version 59.0 and later.
  ForecastingSubmission
  Represents a submitted forecast. This object is available in API version 62.0 and later.
  ForecastingSubmissionItem
  Represents the values for each forecast category in a submitted forecast. This object is available in API version 62.0 and later.
  ForecastingType
  Used to identify the forecast type associated with ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingQuota, ForecastingFact, and ForecastingItem objects. Available in API version 30.0 and greater.
  ForecastingTypeSource
  Maps a forecasting source definition to a forecast type. This object is available in API version 52.0 and later.
  ForecastingUserPreference
  Represents the forecasting selections that a user has made, such as display options, date range, forecasting type, and currency.
  FormulaFunction
  Represents a function used when building a formula, including examples and uses. This object is available in API version 47.0 and later.
  FormulaFunctionAllowedType
  Represents the functions that are supported in the given formula context. This object is available in API version 48.0 and later.
  FormulaFunctionCategory
  Represents the category to which a formula belongs when building a formula. This object is available in API version 47.0 and later.
  FrcstCustmCatgRampRateSrc
  Represents the total contract value used for custom bulk adjustments. This object is available in API version 63.0 and later.
  FulfillmentOrder
  Represents a group of products, fees, and delivery charges on a single order that share the same fulfillment location, delivery method, and recipient. The FulfillmentOrderLineItems belonging to a FulfillmentOrder are associated with OrderItemSummary objects belonging to a single OrderSummary. This object is available in API version 48.0 and later.
  FulfillmentOrderItemAdjustment
  Represents a price adjustment on a FulfillmentOrderLineItem. Corresponds to an OrderItemAdjustmentLineSummary associated with the corresponding OrderItemSummary. This object is available in API version 48.0 and later.
  FulfillmentOrderItemTax
  Represents the tax on a FulfillmentOrderLineItem or FulfillmentOrderItemAdjustment. Corresponds to an OrderItemTaxLineItemSummary. This object is available in API version 48.0 and later.
  FulfillmentOrderLineItem
  Represents a product or delivery charge belonging to a FulfillmentOrder. Corresponds to an OrderItemSummary. This object is available in API version 48.0 and later.
  FunctionConnection
  Represents a connection between an org and Salesforce Functions. This object is available in API version 52.0 and later.
  FunctionInvocationRequest
  Represents invocation information for a Salesforce Function. This object is available in API version 51.0 and later.
  FunctionReference
  Represents a deployed Salesforce Function associated with an org. This object is available in API version 52.0 and later.
  GenAIConversationSummary
  Represents a generated summary of a voice or video call. This object is available in API version 60.0 and later.
  GenAiFunctionDefinition
  Represents a copilot action that can be added to Einstein Copilot. This object is available in API version 60.0 and later.
  GenAiPlannerDefinition
  Represents a copilot planner service that uses a large language model (LLM) and a reasoning strategy to decompose a given task into smaller subtasks, identify the most suitable actions for each subtask, and invoke them. This object is available in API version 60.0 and later.
  GenAiPlannerFunctionDef
  Represents a relationship between the copilot planner service and copilot actions. This object is available in API version 60.0 and later.
  GenAiPluginDefinition
  Represents an agent topic, which is a category of actions related to a particular job to be done by AI agents. This object is available in API version 62.0 and later.
  GeoCountry
  Represents a country. This object is available in API version 56.0 and later.
  GeolocationBasedAction
  Represents a geolocation-based action, which is an action that’s triggered when a user enters, exits, or is within the area of the associated object. Available in API version 61.0 and later.
  GeoState
  Represents a state. This object is available in API version 57.0 and later.
  GtwyProvPaymentMethodType
  The gateway provider payment method type allows integrators and payment providers to choose an active payment to receive an order's payment data rather than allowing the Salesforce Order Management platform to select a default payment method. This object is available in API version 50.0 and later.
  Goal
  The Goal object represents the components of a goal such as its name, description, and status.
  GoalLink
  Represents the relationship between two goals. This is a many-to-many relationship, meaning that each goal can link to many other goals.
  GoogleDoc
  Represents a link to a Google Document. This object is available in API version 14.0 and later.
  Group
  A set of User records.
  GroupMember
  Represents a User or Group that is a member of a public group.
  GuestBuyerProfile
  Represents a store's guest buyer profile, which allows unauthenticated buyers to browse the store. This object is available in API version 51.0 and later.
  HashtagDefinition
  HashtagDefinition represents hashtag (#) topics in public Chatter posts and comments. Public posts and comments include those on profiles and in public groups, but not those on records or in private groups. This object is available in API version 26.0 and later.
  HealthCareDiagnosis
  Represents information related to industry-standard healthcare diagnosis codes.
  HealthCareProcedure
  Represents information related to industry-standard healthcare procedure codes.
  Holiday
  Represents a period of time during which your customer support team is unavailable. Business hours and escalation rules associated with business hours are suspended during any holidays with which they are affiliated.
  IconDefinition
  Represents the icon-related metadata for a custom tab. This object is available in API version 43.0 and later.
  Idea
  Represents an idea on which users are allowed to comment and vote, for example, a suggestion for an enhancement to an existing product or process. This object is available in API version 12 and later.
  IdeaComment
  Represents a comment that a user has submitted in response to an idea.
  IdeaReputation
  Represents a collection of statistics and scores derived from a user’s activity within an Ideas zone or internal organization. This object is available in API version 28.0 and later.
  IdeaReputationLevel
  Represents a reputation level within an Ideas zone or internal organization and is used by the system to calculate reputation. You can create up to 25 levels per zone or internal organization. This object is available in API version 28.0 and later.
  IdeaTheme
  Represents an invitation to zone members to submit ideas that are focused on a specific topic. This object is available in API version 26 and later.
  IdpEventLog
  Represents the Identity Provider Event Log. This log records both problems and successes with inbound SAML or OpenID Connect authentication requests from another app provider. It also records outbound SAML responses when Salesforce is acting as an identity provider. This object is available in API version 39.0 and later.
  IframeWhiteListUrl
  Represents a list of trusted external domains that you allow to frame your Embedded Service, Surveys, and Visualforce pages. This object is available in API version 45.0 and later.
  Image
  Represents the details of an image. This object is available in API version 47.0 and later.
  Incident
  An Incident is any unplanned business interruption that has wide-sweeping impacts and requires an urgent fix. This object contains the details of the incident, documenting the history of the incident from registration to closure. This object is available in API version 53.0 and later.
  IncidentRelatedItem
  Represents a junction object that relates an Incident to an Asset or Product. This object is available in API version 53.0 and later.
  Individual
  Represents a customer’s data privacy and protection preferences. Data privacy records based on the Individual object store your customers’ preferences. Data privacy records are associated with related leads, contacts, person accounts, and users. This object is available in API version 42.0 and later.
  IndividualApplicationItem
  Captures individual application input data that is used during run-time. This object is available in API version 58.0 and later.
  IndividualHistory
  Represents the history of changes to values in the fields of a data privacy record, based on the Individual object. This object is available in versions 42.0 and later.
  IndividualShare
  Represents a list of access levels to a data privacy record along with an explanation of the access level. For example, if you have access to a record because you own it, the IndividualAccessLevel is All and RowCause is Owner. This object is available in API version 42.0 and later.
  InsufficientAccessEventLog
  Insufficient Access event logs contain details about errors relating to insufficient record access This object is available in API version 61.0 and later.
  InternalOrganizationUnit
  Represents an organization that an Employee belongs to. This object is available in API version 48.0 and later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.
  InventoryItemReservation
  Used to store inventory item reservation information for a specific product and location. This object is available in API version 60.0 and later.
  InventoryReservation
  Stores information about the status of cart inventory reservations in B2B and D2C Commerce. This object is available in API version 60.0 and later.
  Invoice
  Represents a financial document describing the total amount a buyer must pay for goods or services provided. This object is available in API version 48.0 and later.
  InvoiceAddressGroup
  Stores the buyer's address information. This object is available in API version 50.0 and later.
  InvoiceBatchRun
  Represents a batch processing job in Subscription Management or Revenue Lifecycle Management Billing. During an invoice batch run, all billing schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version 55.0 and later.
  InvoiceBatchRunCriteria
  Represents a batch processing job and its required criteria in Subscription Management. During an invoice batch run, all billing schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version 55.0 and later.
  InvoiceBatchRunRecovery
  Provides information about an invoice batch run recovery procedure. This object is available in API version 57.0 and later.
  InvoiceDocument
  Tracks and displays the status of documents generated for invoices. Invoice documents are available in the related lists of invoice entity records. This object is available in API version 61.0 and later.
  InvoiceLine
  Represents the amount that a buyer must pay for a product, service, or fee. Invoice lines are created based on the amount of an order line. This object is available in API version 48.0 and later.
  JobProfile
  Represents a job profile used for shift scheduling. This object is available in API versions 47.0 and later.
  JobProfileQueueGroup
  JobProfileQueueGroup defines the mapping between Queue and JobProfile and configurations for capacity plans in Workforce Engagement. This object is available in API version 53.0 and later.
  Knowledge__Feed
  Represents the feed for a knowledge article. This object is available in API version 39.0 and later.
  Knowledge__ka
  Provides access to the concrete object that represents a Knowledge article, the parent object for article versions. This object is available in API version 39.0 and later.
  Knowledge__kav
  Provides access to the concrete object that represents a Knowledge article version. This object is available in API version 39.0 and later.
  Knowledge__DataCategorySelection
  Represents a data category that classifies an article. This object is available in API version 39.0 and later.
  KnowledgeableUser
  Represents a user identified as knowledgeable about a specific topic, and ranks them relative to other knowledgeable users. This object is available in API version 31.0 and later.
  KnowledgeArticle
  Provides read-only access to an article and the ability to delete the primary article. This object is available in API version 19.0 and later.
  KnowledgeArticleEventLog
  Knowledge Article View event logs contain user activity with your knowledge base. This object is available in API version 55.0 and later.
  KnowledgeArticleVersion
  Provides a global view of standard article fields across all types of articles depending on their version. This object is available in API version 18.0 and later.
  KnowledgeArticleVersionHistory
  Enables read-only access to the full history of an article. This object is available in API version 25.0 and later.
  KnowledgeArticleViewStat
  Provides certain statistics related to the number of views for the specified article across all article types. The view count statistics are for published and archived articles only. View counts for draft articles aren’t tracked. This object is read-only and available in API version 20.0 and later.
  KnowledgeArticleVoteStat
  Provides the weighted rating for the specified article on a scale of 1 to 5 across all article types. This object is read-only and available in API version 20.0 and later.
  LandingPage
  Represents an Account Engagement landing page. A landing page is a web page that a visitor reaches after clicking a link or advertisement. Landing pages can be created in Account Engagement and synced to Salesforce or created on the Landing Page object in Account Engagement Lightning App. This object is available in API version 42.0 and later.
  Lead
  Represents a prospect or lead.
  LeadCleanInfo
  Stores the metadata Data.com Clean uses to determine a lead record’s clean status. Helps you automate the cleaning or related processing of lead records.
  LeadDailyMetric
  Represents the daily engagement metrics for a lead. This object is available in API version 52.0 and later.
  LeadMonthlyMetric
  Represents the monthly engagement metrics for a lead. This object is available in API version 52.0 and later.
  LeadOwnerSharingRule
  Represents the rules for sharing a lead with users other than the owner.
  LeadShare
  Represents a sharing entry on a Lead.
  LeadStatus
  Represents the status of a Lead record, such as Open, Qualified, or Converted.
  LeadTag
  Associates a word or short phrase with a Lead.
  LearningContent
  Represents a Trailhead or enablement site (myTrailhead) module assigned to a user in Workforce Engagement or Learning Paths. This object also represents a Trailhead module or video in an Enablement program exercise. This object is available in API version 54.0 and later.
  LearningItem
  Represents an item that requires users to take action, including a Learning Paths entry, an Enablement program, or an exercise with linked content in an Enablement program. For Learning Paths, users are assigned a learning item to complete. For Enablement programs and exercises, users are assigned a program or can self-enroll in shared programs. This object is available in API version 58.0 and later.
  LearningItemAssignment
  Represents the assignment of a Learning Paths entry to users or groups or the enrollment of an Enablement program for a specific user. This object is available in API version 58.0 and later.
  LearningItemProgress
  Represents the progress that a user has made towards completing an assigned learning item, such as a Learning Paths entry or Enablement program. This object is available in API version 60.0 and later.
  LearningItemSubmission
  Represents a link to a resource, such as a video recording, that a user submits as part of a Feedback Request exercise in an Enablement program. For peer and manager feedback, this resource can be a recording of a user’s sales patch. For Einstein Coach feedback, this resource can be a video call, and Einstein generates feedback from the call’s transcription. This object is available in API version 59.0 and later, but Einstein Coach is available only in API version 61.0 and later.
  LearningItemType
  Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom exercise type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition and EnblProgramTaskSubCategory records for when admins create a program in Program Builder. This object is available in API version 62.0 and later.
  LearningPractice
  Represents a Feedback Request exercise in an Enablement program. Users can submit a sample of their work and request feedback from their peers and managers. Or, users can submit a video call and Einstein Coach generates feedback from the call’s transcription. This object is available in API version 59.0 and later, but Einstein Coach feedback is available only in API version 61.0 and later.
  LegalEntity
  Represents the way an organization is structured. An organization can be a single legal entity or it can comprise more than one legal entity. This object is available in API version 48.0 and later.
  LicenseDefinitionCustomPermission (Developer Preview)
  Represents a licensed custom permission that controls access to a license's features when included in a custom permission set license definition. This object is available in API version 54.0 and later.
  LightningExperienceTheme
  Represents information for a theme in Lightning Experience. This object is available in API Version 42.0 and later.
  LightningLoggerEventLog
  Lightning Logger Event Log provides information from observed Lightning component logs. This object is available in API version 61.0 and later.
  LightningOnboardingConfig
  Represents the feedback provided when users switch from Lightning Experience to Salesforce Classic. Admins can customize the question, how frequently the form appears, and where the feedback is stored in Chatter from the Adoption Assistance page in Lightning Experience Setup. Available in API version 47.0 and later.
  LightningPageViewEventLog
  Lightning Page View event logs represent information about the page on which the event occurred in Lightning Experience and the Salesforce mobile app. A Lightning Page View event log tracks the page a user visited, how long the user spent on the page, and the load time for the page. This object is available in API version 55.0 and later.
  LightningToggleMetrics
  Represents users who switched from Lightning Experience back to Salesforce Classic. This object is available in API version 43.0 and later.
  LightningUsageByAppTypeMetrics
  Represents number of users on Lightning Experience and Salesforce Mobile. This object is available in API version 43.0 and later.
  LightningUsageByBrowserMetrics
  Represents Lightning Experience usage grouped by user’s browser. This object is available in API version 43.0 and later.
  LightningUsageByPageMetrics
  Represents standard pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.
  LightningUsageByFlexiPageMetrics
  Represents custom pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.
  LightningExitByPageMetrics
  Represents frequency metrics about the standard pages within which users switched from Lightning Experience to Salesforce Classic. This object is available in API version 44.0 and later.
  LinkedArticle
  Represents a knowledge article that is attached to a work order, work order line item, or work type. This object is available in API version 37.0 and later.
  LinkedArticleFeed
  Represents the comment feed on a linked article. This object is available in API version 39.0 and later.
  LinkedArticleHistory
  Represents the history of changes made to tracked fields on a linked article. This object is available in API version 37.0 and later.
  ListEmail
  Represents a list email sent from Salesforce, or sent from Account Engagement and synced to Salesforce. When the list email is sent, the recipients are generated by combining recipients in ListEmailIndividualRecipients and ListEmailRecipientSource. Duplicate and other invalid recipients are removed. The result is the recipients sent any given list email. ListEmail has a one-to-many relationship with ListEmailRecipientSource and ListEmailIndividualRecipient. This object is available in API version 41.0 and later.
  ListEmailIndividualRecipient
  For a list email in Salesforce, represents a recipient. Each record represents a link from a list email to exactly one recipient for that list email. Recipients can be contacts, leads, or campaign members. Has a one-to-many relationship with ListEmail. This object is available in API version 44.0 and later.
  ListEmailMonthlyMetric
  Represents the monthly engagement metrics for a single list email. This object is available in API version 49.0 and later.
  ListEmailRecipientSource
  For a list email in Salesforce, represents the dynamically defined sources of recipient email addresses. Each record represents a link to a single list view or campaign that is examined when the list email is sent. Has a one-to-many relationship with ListEmail. This object is available in API version 41.0 and later.
  ListView
  Represents a list view. A list view shows a set of records for an object, based on specific criteria. This object is available in API version 32.0 and later.
  ListViewChart
  Represents a graphical chart that’s displayed on Salesforce for Android, iOS, and mobile web list views. The chart aggregates data that is filtered based on the list view that’s currently displayed. This object is available in API version 33.0 and later and is accessible by portal users.
  ListViewChartInstance
  Retrieves metadata for all standard and custom charts for a given entity in context of a given list view. This object is available in API versions 34.0 and later.
  LiveAgentSession
  This object is automatically created for each Chat session and stores information about the session. This object is available in API versions 28.0 and later.
  LiveAgentSessionHistory
  This object is automatically created for each Chat session and stores information about changes made to the session. This object is available in API versions 28.0 and later.
  LiveAgentSessionShare
  This object is automatically created for each Chat session and stores information about the session. This object is available in API versions 28.0 and later.
  LiveChatBlockingRule
  Represents a rule for blocking chat visitors’ IP addresses from starting new chats with agents. This object is available in API version 34.0 and later.
  LiveChatObjectAccessConfig
  Represents the action you can perform on a specified object by the Chat API. This object is available in API version 53.0 and later.
  LiveChatObjectAccessDefinition
  Represents the parent record for one or more LiveChatObjectAccessConfig objects. This object is available in API version 53.0 and later.
  LiveChatButton
  Represents a button that allows visitors to request chats with Chat users. This object is available in API version 24.0 and later.
  LiveChatButtonDeployment
  Associates an automated chat invitation with a specific deployment. This object is available in API versions 28.0 and later.
  LiveChatButtonSkill
  Represents all the skills available to a LiveChatButton except the one currently assigned. To retrieve the skill currently assigned, query LiveChatButton. This object is available in API version 25.0 and later.
  LiveChatDeployment
  Represents the general settings for deploying Live Agent on a website. This object is available in API version 24.0 and later.
  LiveChatSensitiveDataRule
  Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex). This object is available in API version 35.0 and later.
  LiveChatTranscript
  This object is automatically created for each Live Agent chat session and stores information about the session. This object is available in API version 24.0 and later.
  LiveChatTranscriptEvent
  Captures specific events that occur over the lifetime of a chat. This object is available in API version 24.0 and later.
  LiveChatTranscriptShare
  Represents a sharing entry on a LiveChatTranscript object. This object is available in API version 24.0 and later.
  LiveChatTranscriptSkill
  Represents a join between LiveChatTranscript and Skill. This object is available in API version 25.0 and later.
  LiveChatUserConfig
  Represents a setting that controls the console settings for Chat users. This object is available in API version 24.0 and later.
  LiveChatUserConfigProfile
  Represents a join between LiveChatUserConfig and Profile. This object is available in API version 24.0 and later.
  LiveChatUserConfigUser
  Represents a join between Live Chat User Config and User. This object is available in API version 24.0 and later.
  LiveChatVisitor
  Represents a website visitor who has started or tried to start a chat session. This object is available in API version 24.0 and later.
  Location
  Represents a warehouse, service vehicle, work site, or other element of the region where your team performs field service work. In API version 49.0 and later, you can associate activities with specific locations. Activities, such as the tasks and events related to a location, appear in the activities timeline when you view the location detail page. Also in API version 49.0 and later, Work.com users can view Employees as a related list on Location records. In API version 51.0 and later, this object is available for Omnichannel Inventory and represents physical locations where inventory is available for fulfilling orders.
  LocationGroup
  Represents a group of Omnichannel Inventory locations, providing an aggregate view of inventory availability across those locations. Omnichannel Inventory can create an inventory reservation for an order at the location group level, then assign the reservation to one or more locations in the group as needed. This object is available in API version 51.0 and later.
  LocationGroupAssignment
  Represents the assignment of a location to a location group. This object is available in API version 51.0 and later.
  LocationShippingCarrierMethod
  The available shipping carrier services associated with a location or location group. Allows the assignment of different shipping methods to a specific location and enables flexibility and customization in the shipping process. This object is available in API version 61.0 and later.
  LocationTrustMeasure
  Represents the COVID safety protocols that your business follows. For example, enforcement of masks, social distancing, cleanliness, and capacity limits. This object is available in API version 50.0 and later.
  LocWaitlistMsgTemplate
  Represents a junction object connecting LocationWaitlist to MessagingTemplate. This object is available in API version 50.0 and later.
  LocationWaitlist
  Represents a queue created for a specific location. Multiple queues can be created for a single location. For example, you can have a queue for each sales agent or a standard queue and a queue for vulnerable groups. The specific party of people in a queue is represented by LocationWaitlistedParty. This object is available in API version 50.0 and later.
  LocationWaitlistedParty
  Represents a specific party of people waiting in a queue. This object is available in API version 50.0 and later.
  LoginAsEventLog
  LoginAsEventLog contains details about when a user logs in as another user in your org. This object is available in API version 56.0 and later.
  LoginEvent
  The documentation has moved to LoginEvent in the Platform Events Developer Guide.
  LoginEventLog
  Login event logs contain details about your Salesforce org's user login history. This object is available in API version 55.0 and later.
  LoginGeo
  Represents the geographic location of the user’s IP address for a login event. Due to the nature of geolocation technology, the accuracy of geolocation fields (for example, country, city, postal code) may vary. This object is available in API version 34.0 and later.
  LoginHistory
  Represents the login history for all successful and failed login attempts for organizations and enabled portals. This object is available in API version 21.0 and later.
  LoginIp
  Represents a validated IP address. This object is available in version 28.0 and later.
  LogoutEventStream
  The documentation has moved to LogoutEventStream in the Platform Events Developer Guide.
  LookedUpFromActivity
  This read-only object is displayed as a related list on an activity record (an event or a task); the list contains records that have custom lookup relationships from the activity to another object. This object is not queryable.
  Macro
  Represents a macro, which is a set of instructions that tells the system to perform one or more tasks. This object is available in API version 32.0 and later.
  MacroInstruction
  Represents an instruction in a macro. An instruction can specify the object that the macro interacts with, the context or publisher that the macro works within, the operation or action that the macro performs, and the target of the macro’s actions.
  MacroUsage
  Represents macro usage on a record, including which macro was used, who used it, and how they used it. This object is available in API version 47.0 and later.
  MailmergeTemplate
  Represents a mail merge template (a Microsoft Word document) used for performing mail merges for your organization.
  MaintenanceAsset
  Represents an asset covered by a maintenance plan in field service. Assets can be associated with multiple maintenance plans.
  MaintenancePlan
  Represents a preventive maintenance schedule for one or more assets in field service.
  MaintenanceWorkRule
  Represents the recurrence pattern for a maintenance record. This object is available in API version 49.0 and later.
  ManagedContent
  Represents managed content in a Salesforce CMS workspace for use in an Experience Cloud site or a channel. The ManagedContent object represents the complete instance of a managed content record. It provides a consistent identifier for the managed content so that variants of the content item can be created over time. This object is available in API version 56.0 and later.
  ManagedContentChannel
  Represents the details of a CMS channel. CMS channels correspond to managed content publishing endpoints. They deliver published content from your Salesforce CMS workspaces to an audience. This object is available in API version 55.0 and later.
  ManagedContentInfo
  Allows the creation of relationship to Product using ProductMedia. This object is available in API version 49.0 to 57.0. In API version 58.0 and later, use the ManagedContent object.
  ManagedContentSpace
  Represents the complete instance of a Salesforce CMS workspace that stores managed content. Users and groups with designated permissions can access and manage the content in a CMS workspace. This object is available in API version 56.0 and later.
  ManagedContentVariant
  Represents a variant of a managed content item. This object is available in API version 56.0 and later.
  MarketingForm
  Represents an Account Engagement marketing form that has been synched to Salesforce. Use forms on your website and landing pages to collect information about visitors and turn anonymous visitors into identified prospects. This object is available in API version 42.0 and later.
  MarketingLink
  Represents an Account Engagement marketing link record, either a custom redirect or a file, that has been synced to Salesforce. This object is available in API version 42.0 and later.
  MatchingRule
  Represents a matching rule that is used to identify duplicate records. This object is available in API version 33.0 and later.
  MatchingRuleItem
  Represents criteria used by a matching rule to identify duplicate records. This object is available in API version 33.0 and later.
  MediaChannel
  Defines a web page, a TV program, or a publication. A media channel may contain one to many Ad Spaces, into which Ad Servers can place or serve up ad creatives. This object is available in API version 54.0 and later.
  MediaContentTitle
  Stores details about an event or show that may be broadcast on TV or radio channels. This object is available in API version 54.0 and later.
  MediaPrintIssue
  Represents the details of an issue with details such as issue name, date, advertising deadline about the publication. It is specific to Print media channels in Ad Sales and is available periodically based on publication frequency. This object is available in API version 57.0 and later.
  MerchAccPaymentMethodSet
  Defines an ordered list of payment methods that are available to a merchant's cudstomer during checkout. You can configure multiple payment method sets, each designated for a specific locale, payment region, or sale channel. This object is available in API version 58.0 and later.
  MerchAccPaymentMethodType
  Refers to a payment method that is in a payment method set, which is defined by the MerchAccPaymentMethodSet object. This object is available in API version 58.0 and later.
  MerchantAccount
  A type of bank account that lets a merchant accept payments from a variety of payment methods, including credit or debit cards, or digital wallets. A Salesforce Payments merchant account is linked to an underlying payment gateway to process payments This object is available in API version 56.0 and later.
  MerchantAccountEvent
  Represents a merchant account platform event. Subscribe to these events so you can listen and respond to them when they’re published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0 and later.
  MessagingChannel
  Represents a communication channel that an end user can use to send a message to an agent. A communication channel can be an SMS number, a Facebook page, or another supported messaging channel. This object is available in API version 40.0 and later.
  MessagingChannelSkill
  Junction object that represents an association between MessagingChannel and Skill. This object is available in API version 45.0 and later.
  MessagingChannelUsage
  Represents the status of an enhanced Messaging channel or of an application in a Unified Messaging channel. This object is available in API version 60.0 and later.
  MessagingConfiguration
  Represents the details for a Messaging configuration. This object is available in API version 47.0 and later.
  MessagingDeliveryError
  Represents a log of triggered outbound failures to verify when a triggered outbound has failed. This object is available in API version 44.0 and later.
  MessagingEndUser
  Represents a single address—such as a phone number or Facebook page—communicating with a single Messaging channel. This object is available in API version 40.0 and later.
  MessagingLink
  Represents the link between a Messaging Channel and where it's shared. This object is available in API version 47.0 and later.
  MessagingSession
  Represents a session on a Messaging channel. This object is available in API version 47.0 and later.
  MessagingSessionMetrics
  Represents a metric gathered about a specific enhanced messaging session, such as average agent response time. This object is available starting in October 2024 in API version 62.0 and later.
  MessagingTemplate
  Represents a Messaging template used to send pre-formatted messages. This object is available in API version 47.0 and later.
  MetadataApiOpEventLog
  MetadataApiOpEventLog stores details of Metadata API retrieval and deployment requests. This object is available in API version 62.0 and later.
  MetadataPackage
  Represents a package that has been developed in the org you’re logged in to. Applies to unlocked, unmanaged, first-generation, and second-generation managed packages.
  MetadataPackageVersion
  Represents a package version (managed or unmanaged) that has been uploaded from the org you’re logged in to.
  Metric
  The Metric object represents the components of a goal metric such as its name, metric type, and current value.
  MetricDataLink
  The link between the metric and the data source, such as a report.
  MilestoneType
  Represents a milestone (required step in a customer support process). This object is available in API version 18.0 and later.
  MLField
  Represents a single field in a data definition. This object is available in API version 50.0 and later.
  MlIntentUtteranceSuggestion
  Represents a customer input, used for training purposes in the feedback loop process of a conversation. Admins can add these inputs to the intent training model. This object is available in API version 51.0 and later.
  MLPredictionDefinition
  Represents a prediction definition that specifies details about the prediction. This object is available in API version 50.0 and later.
  MLModel
  Represents an AI model that can be used in Einstein Prediction Builder, Einstein Recommendation Builder, and other Einstein features. This object is available in API version 53.0 and later.
  MLModelFactor
  Represents a field value that has a positive or negative effect on the model’s score. This object is available in API version 53.0 and later.
  MLModelFactorComponent
  Represents information about the related MLModelFactor. For example, this object can represent a field value or a field range such as “Title = CEO” or “Annual Revenue >10000000”. This object is available in API version 53.0 and later.
  MLModelMetric
  Represents a metric or statistic about the related model, such as accuracy, precision, or RSquared. Use a model’s metrics to learn about its performance and to compare it with other models. This object is available in API version 53.0 and later.
  MLRecommendationDefinition
  For internal use only.
  MobileSecurityAssignment
  Represents the assignment of mobile security policies to a profile. The policies apply to the Salesforce mobile app with Enhanced Mobile App Security enabled. This object is available in API version 54.0 and later.
  MobileSecurityPolicy
  Enables mobile security policies on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version 50.0 and later.
  MobileSecurityUserMetric
  Represents the metrics for users who have Enhanced Mobile Security policies enforced. This object is available in API version 51.0 and later.
  MobileSettingsAssignment
  Represents the assignment of a particular field service mobile settings configuration to a user profile. This object is available in API version 41.0 and later.
  MobSecurityCertPinConfig
  Configuration of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version 53.0 and later.
  MobSecurityCertPinEvent
  The event of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version 53.0 and later.
  MsgChannelLanguageKeyword
  Represents the consent configuration for a Messaging channel. This object is available in API version 48.0 and later.
  MsgChannelUsageExternalOrg
  Represents the Enterprise ID (EID) and Business Unit (MID) for Marketing Cloud connections in a Unified Messaging channel. This object is available in API version 60.0 and later.
  MyDomainDiscoverableLogin
  Represents configuration settings when the My Domain login page type is Discovery. Login Discovery provides an identity-first login experience, where the login page contains the identifier field only. Based on the identifier entered, a handler determines how to authenticate the user. This object is available in API version 45.0 and later.
  MutingPermissionSet
  Represents a set of disabled permissions and is used in conjunction with PermissionSetGroup. This object is available in API version 46.0 and later.
  Name
  Non-queryable object that provides information about foreign key traversals when the foreign key has more than one parent.
  NamedCredential
  Represents a named credential, which specifies the URL of a callout endpoint and its required authentication parameters in one definition. A named credential can be specified as an endpoint to simplify the setup of authenticated callouts. This object is available in API version 33.0 and later.
  NamespaceRegistry
  Represents a namespace that you can link to scratch orgs that were created from your org’s Dev Hub. You use the namespace when developing, packaging, and releasing an app. You can’t create this object with the API. Use the Link Namespace action in the Dev Hub graphical interface to insert a NamespaceRegistry record. This object is available in API version 41.0 and later.
  NavigationLinkSet
  Represents the navigation menu in an Experience Cloud site. A navigation menu consists of items that users can click to go to other parts of the site. This object is available in API version 35.0 and later.
  NavigationMenuItem
  Represents a single menu item in a NavigationLinkSet. Use this object to create, delete, or update menu items in your Experience Cloud site’s navigation menu. This object is available in API version 35.0 and later.
  NavigationMenuItemLocalization
  Represents the translated value of a navigation menu item in an Experience Cloud site. This object is available in API version 36.0 and later.
  Network
  Represents an Experience Cloud site. Salesforce Experience Cloud lets you create branded spaces for your employees, customers, and partners. You can customize and create experiences, whether they’re communities, sites, or portals, to meet your business needs, then transition seamlessly between them. Experience Cloud sites let you share information, records, and files with coworkers and stakeholders all in one place. This object is available in API version 26.0 and later.
  NetworkActivityAudit
  Represents an audit trail of moderation actions in Experience Cloud sites. This object is available in API version 30.0 and later.
  NetworkAffinity
  Represents a junction object that associates a user profile with a Network object, that is, with an Experience Cloud site. Use NetworkAffinity to assign a default Experience Cloud site to a user profile. This object is available in API version 41.0 and later.
  NetworkAuthApiSettings
  Represents the settings that control enablement, access, and security for the Headless Registration Flow, Headless Forgot Password Flow, Headless Passwordless Login Flow, and their associated APIs. This object is available in API version 58.0 and later.
  NetworkDataCategory
  Represents data categories in Lightning Web Runtime (LWR) Experience Cloud Sites. This object is available in API version 59.0 and later.
  NetworkDiscoverableLogin
  Represents the Login Discoverable page from where customers and partners log in to an Experience Cloud site. Customers and partners are users with an External Identity license or any communities license for Experience Cloud. This object is available in API version 44.0 and later.
  NetworkEmailTmplAllowlist
  Represents an allowlist for the one-time password (OTP) email templates that are sent to end users during the Headless Registration Flow, the Headless Passwordless Login Flow, and the Headless Forgot Password Flow. This object is available in API version 60.0 and later.
  NetworkFeedResponseMetric
  Represents an object that stores the date and time values of question posts. It captures information for question creation, answer creation, and when an answer is marked as best answer This object is available in API version 51.0 and later.
  NetworkMember
  Represents a member of an Experience Cloud site. Members can be either users in your company or external users with portal profiles. This object is available in API version 26.0 and later.
  NetworkMemberGroup
  Represents a group of members in an Experience Cloud site. Members can be either users in your internal org or external users assigned portal profiles. An administrator adds members to an Experience Cloud site by adding a profile or a permission set, and any user with the profile or permission set becomes a member of the site. This object is available in API version 26.0 and later.
  NetworkModeration
  Represents a flag on an item in a community. This object is available in API version 30.0 and later.
  NetworkPageOverride
  Represents information about custom pages used to override the default pages in Experience Cloud sites. You can create Experience Builder or Visualforce pages and override the default pages in a site. Using custom pages allows you to create a more personalized experience for your users. This object is available in API version 34.0 and later.
  NetworkSelfRegistration
  Represents the account that self-registering Experience Cloud users are associated with by default. Self-registering users in an Experience Cloud site are required to be associated with an account, which the admin must specify while setting up self-registration for the site. If an account isn’t specified, Salesforce creates person accounts (when enabled) for self-registering users. This object is available in API version 34.0 and later.
  NetworkUserHistoryRecent
  Represents an Experience Cloud site user’s history of accessed records. This object is available in API version 42.0 and later.
  Note
  Represents a note, which is text associated with a custom object or a standard object, such as a Contact, Contract, or Opportunity.
  NoteAndAttachment
  This read-only object contains all notes and attachments associated with an object.
  NoteTag
  Associates a word or short phrase with a Note.
  OauthCustomScope
  Represents a permission defining the protected data that a connected app can access from an external entity when Salesforce is the OAuth authorization provider.
  OauthCustomScopeApp
  Represents the name of the connected app to which the custom scope is assigned. This object is available in API version 49.0 and later.
  OauthToken
  Represents an OAuth access token for connected app authentication. Use this object to create a user interface for token management. This object is available in API version 32.0 and later.
  OauthTokenExchangeHandler
  Represents a token exchange handler. The token exchange handler also consists of an Apex class. During the OAuth 2.0 token exchange flow, the token exchange handler is used to validate tokens from an external identity provider and to map users to Salesforce. This object is available in API version 60.0 and later.
  OauthTokenExchHandlerApp
  Represents the enablement settings for a specific Salesforce connected app or external client app that’s enabled for the token exchange handler. A handler can be enabled for multiple apps. This object is available in API version 60.0 and later.
  ObjectDataImport
  Represents the data import status of one or more object records. This object is available in API version 57.0 and later.
  ObjectDataImportReference
  Represents the relationships to the associated reference objects showing the source from which the data is imported. This object is available in API version 57.0 and later.
  ObjectMetadataTag
  Represents a meta tag for a store page. Meta tags in HTML documents provide structured data used by search engines for ranking and to show content in search results. This object is available in API version 60.0 and later.
  ObjectPermissions
  Represents the enabled object permissions for the parent PermissionSet. This object is available in API version 24.0 and later.
  ObjectRelatedUrl
  Represents a URL slug for a Product or Category page on a B2B Commerce or D2C Commerce LWR site, or a custom object, account, or contact page on an enhanced LWR Experience Cloud site. This object is available in API version 57.0 and later.
  ObjectTerritory2AssignmentRule
  Represents a territory assignment rule that’s associated with an object, such as Account. ObjectTerritory2AssignmentRuleItem can be created or deleted if the BooleanFilter field on its corresponding ObjectTerritory2AssignmentRule is null. Available if Sales Territories has been enabled.
  ObjectTerritory2AssignmentRuleItem
  A single row of selection criteria for an ObjectTerritory2AssignmentRule object. ObjectTerritory2AssignmentRuleItem can only be created or deleted if the BooleanFilter field on its corresponding ObjectTerritory2AssignmentRule object is a null value. Available if Sales Territories has been enabled.
  ObjectTerritory2Association
  Represents an association (by assignment) between a territory and an object record such as an account or a lead.
  ObjectUserTerritory2View
  Represents a user and object, such as an account or lead, assigned to a territory. This object is available in API version 58.0 and later.
  OmniDataPack
  For internal use only.
  OmniDataTransform
  For internal use only.
  OmniDataTransformItem
  For internal use only.
  OmniESignature
  For internal use only.
  OmniExtTrackingDef
  Represents a connection between an OmniTrackingGroup in OmniAnalytics and a third-party Analytics system such as Google Analytics. This object is available in API version 60.0 and later.
  OmniExtTrackingEventDef
  Represents a format for FlexCard or OmniScript user interaction data that a third-party Analytics system such as Google Analytics can accept. This object is available in API version 60.0 and later.
  OmniInteractionConfig
  For internal use only.
  OmniInteractionAccessConfig
  For internal use only.
  OmniProcess
  For internal use only.
  OmniProcessCompilation
  For internal use only.
  OmniProcessElement
  For internal use only.
  OmniProcessTransientData
  For internal use only.
  OmniScriptSavedSession
  For internal use only.
  OmniSupervisorConfig
  Represents the Omni-Channel supervisor configuration for an assigned group of supervisors. This object is available in API version 41.0 and later.
  OmniSupervisorConfigAction
  Represents the actions available to the supervisors of an Omni-Channel supervisor configuration. This object is available in API version 56.0 and later.
  OmniSupervisorConfigGroup
  Represents the group of agents who are visible to the supervisors of an Omni-Channel supervisor configuration. The group, if visible, appears in the Agents tab of Omni Supervisor. This object is available in API version 41.0 and later.
  OmniSupervisorConfigProfile
  Represents the supervisor profiles to which an Omni-Channel supervisor configuration applies. User-level configurations override profile-level configurations. This object is available in API version 41.0 and later.
  OmniSupervisorConfigQueue
  Represents the queues that are visible to the supervisors of an Omni-Channel supervisor configuration. The queue, if visible, appears in the Queues Backlog and Assigned Work tabs of Omni Supervisor. This object is available in API version 53.0 and later.
  OmniSupervisorConfigSkill
  Represents the skills that are visible to the supervisors of an Omni-Channel supervisor configuration. These skills, if visible, appear in the Skills Backlog tab of Omni Supervisor. This object is available in API version 53.0 and later.
  OmniSupervisorConfigTab
  Represents the visible tabs specified in an Omni Supervisor configuration. This object is available in API version 60.0 and later.
  OmniSupervisorConfigUser
  Represents the users to which an Omni-Channel supervisor configuration applies. User-level configurations override profile-level configurations. This object is available in API version 41.0 and later.
  OmniTrackingComponentDef
  Represents a FlexCard or OmniScript that is a member of an OmniTrackingGroup, which tracks user interactions in OmniAnalytics. This object is available in API version 60.0 and later.
  OmniTrackingGroup
  Represents a group of FlexCard and OmniScript components that have their user interactions tracked together in OmniAnalytics. This object is available in API version 60.0 and later.
  OmniUiCard
  For internal use only.
  OpenActivity
  This read-only object is displayed in a related list of open activities—future events and open tasks—related to an object. It includes activities for all contacts related to the object. OpenActivity fields for phone calls are only available if your organization uses Salesforce CRM Call Center.
  OperatingHours
  Represents the hours in which a service territory, service resource, or account is available for work. OperatingHours is used by Field Service, Salesforce Scheduler, Salesforce Meetings, Sales Engagement, and Workforce Engagement. This object is available in API version 38.0 and later.
  OperatingHoursHistory
  Represents the history of changes made to tracked fields on an operating hours record. This object is available in API version 38.0 and later.
  OperatingHoursHoliday
  Represents the day or hours for which a service territory and service resources exclusive to the service territory are unavailable in Salesforce Scheduler. This object is available in API version 54.0 and later.
  Opportunity
  Represents an opportunity, which is a sale or pending deal.
  OpportunityCompetitor
  Represents a competitor on an Opportunity.
  OpportunityContactRole
  Represents the role that a Contact plays on an Opportunity.
  OpportunityContactRoleSuggestionInsight
  Represents a suggestion for a new opportunity contact role. Available in API versions 45.0 and later.
  OpportunityFieldHistory
  Represents the history of changes to the values in the fields of an opportunity. This object is available in versions 13.0 and later.
  OpportunityHistory
  Represents the stage history of an opportunity.
  OpportunityInsight
  Represents an individual insight (deal prediction, follow-up reminder, or key moment) related to an opportunity record.
  OpportunityLineItem
  Represents an opportunity line item, which is a member of the list of Product2 products associated with an Opportunity.
  OpportunityLineItemSchedule
  Represents information about the quantity, revenue distribution, and delivery dates for a particular OpportunityLineItem.
  OpportunityLineItemSplit
  Represents information about an opportunity product split, including percentages, amounts, and owner. This object is available in API version 58.0 and later.
  OpportunityOwnerSharingRule
  Represents a rule for sharing an opportunity with users other than the owner.
  OpportunityPartner
  This object represents a partner relationship between an Account and an Opportunity. An OpportunityPartner record is created automatically when a Partner record is created for a partner relationship between an account and an opportunity.
  OpportunityRelatedDeleteLog
  Represents an audit log of the deletion of opportunity-related child records, such as opportunity team members, product splits, or opportunity splits. This object is available in API version 59.0 and later.
  OpportunityShare
  Represents a sharing entry on an Opportunity.
  OpportunitySplit
  OpportunitySplit credits one or more opportunity team members with a portion of the opportunity amount. This object is available in API version 16.0 and later for pilot customers, and version 28.0 and later for others.
  OpportunitySplitType
  OpportunitySplitType provides unique labels and behavior for each split type. This object is available in API version 28.0 and later.
  OpportunityStage
  Represents the stage of an Opportunity in the sales pipeline, such as New Lead, Negotiating, Pending, Closed, and so on.
  OpportunityTag
  Associates a word or short phrase with an Opportunity.
  OpportunityTeamMember
  Represents a User on the opportunity team of an Opportunity.
  OpptyLineItemSplitType
  Represents an opportunity product split type. This object is available in API version 58.0 and later.
  Order
  Represents an order associated with a contract or an account.
  OrderAction
  Indicates the type of order, such as a new sale or a cancellation. This object is available in API version 55.0 and later.
  OrderAdjustmentGroup
  Group containing a set of adjustments applied to an order. This object is available in API version 48.0 and later.
  OrderAdjustmentGroupSummary
  Represents the current properties and state of a group of related price adjustments. Associated with a set of OrderItemAdjustmentLineSummaries that apply to OrderItemSummaries belonging to one OrderSummary. Corresponds to one or more order adjustment group objects, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.
  OrderChangeLog
  Represents a log record of all change requests made to an order post activation. A log record is always one-to-one to change an order request. This object is available in API version 48.0 and later.
  OrderDeliveryGroup
  A group of order items that share a delivery method and address. The delivery method and address are used during the fulfillment process, such as shipping as a gift, downloading, picking up in store, or shipping to a standard address This object is available in API version 48.0 and later.
  OrderDeliveryGroupSummary
  Represents the current properties and state of a group of OrderItemSummaries, belonging to one OrderSummary, to be fulfilled using the same delivery method and delivered to the same address. A single shipment can include them all, but that isn’t guaranteed. Corresponds to one or more order delivery group objects, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.
  OrderDeliveryMethod
  Shows the customizations and options that a buyer selected for their delivery method. This object is available in API version 48.0 and later.
  OrderHistory
  Represents historical information about changes that have been made to the standard fields of the associated order, or to any custom fields with history tracking enabled.
  OrderItem
  Represents an order product that your organization sells.
  OrderItemAdjustmentLineItem
  An adjustment that has been made to an order item. This object is available in API version 48.0 and later.
  OrderItemAdjustmentLineSummary
  Represents the current properties and state of price adjustments on an OrderItemSummary. Corresponds to one or more order item adjustment line item objects, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.
  OrderItemRelationship
  Describes a relationship between order products. This object is available in API version 58.0 and later.
  OrderItemSummary
  Represents the current properties and state of a product or charge on an OrderSummary. Corresponds to one or more order item objects, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.
  OrderItemSummaryChange
  Represents a change to an OrderItemSummary, usually a reduction in quantity due to a cancel or return. Corresponds to a change order item. This object is available in API version 48.0 and later.
  OrderItemSummaryRelationship
  Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order summary objects in a chain of exchange orders. This object is available in API version 60.0 and later. An exchange order is an OrderSummary object whose SourceProcess property is set to Exchange. An original order summary can have an exchange order, which in turn can have yet another exchange order, and so on. The OrderSummaryRelationship object maintains this relationship between OrderSummary objects.
  OrderItemTaxLineItem
  The tax amount that has been applied to an order item. This object is available in API version 48.0 and later.
  OrderItemTaxLineItemSummary
  Represents the current tax on an OrderItemSummary or OrderItemAdjustmentLineSummary. Corresponds to one or more order item tax line items, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.
  OrderItemType
  Shows whether the order product is a product line or charge line. This object is available in API version 48.0 and later.
  OrderOwnerSharingRule
  Represents a rule which determines order sharing access for the order’s owners.
  OrderPaymentSummary
  Represents the current properties and state of payments using a single payment method that are applied to one OrderSummary. This object is available in API version 48.0 and later.
  OrderPaymentSummaryReference
  OrderPaymentSummaryReference is a junction object that allows an order payment summary to be shared with another order summary. This object is available in API version 60.0 and later.
  OrderShare
  Represents a sharing entry on an Order. This object is available in API version 48.0 and later.
  OrderStatus
  Represents the status of the order entity. This object is available in API version 48.0 and later.
  OrderSummary
  Represents the current properties and state of an order. Corresponds to one or more order objects, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.
  OrderSummaryAdditionalInfo
  Stores information related to OrderSummary including context around the order, such as inventory reservation details, order origination, and other values that Einstein uses to perform order analysis. Only reservation details can be stored in this object. This object is available in API version 58.0 and later.
  OrderSummaryRelationship
  Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order summary objects in a chain of exchange orders. This object is available in API version 60.0 and later.
  OrderSummaryRoutingSchedule
  Represents an attempt to route an order summary to one or more inventory locations for fulfillment. You can use it to schedule future attempts and to record completed attempts. This object is available in API version 51.0 and later.
  Organization
  Represents key configuration information for an organization.
  OrgDeleteRequest
  Represents a request to delete a developer edition (DE) org. This object is available in API version 42.0 and later. It is available only in Developer and Database.com editions.
  OrgEmailAddressSecurity
  Defines the assignment of a user profile to an org-wide email address. This object is available in API version 58.0 and later.
  OrgMetric
  Represents a feature or metric that Salesforce Optimizer evaluates. This object is available in API version 47.0 and later.
  OrgMetricScanResult
  Represents data or an item associated with a feature’s results in a Salesforce Optimizer evaluation. For example, for the Custom Field Limit feature, an OrgMetricScanResult object represents an object flagged for approaching the custom field limit. This object is available in API version 47.0 and later.
  OrgMetricScanSummary
  Represents the results summary for a specific feature in a Salesforce Optimizer evaluation. This object is available in API version 47.0 and later.
  OrgSnapshot
  Represents a snapshot of a scratch org. Snapshots capture the state of a scratch org so that you can use it to quickly spin up new scratch orgs using its configuration. This object is available in API version 61.0 and later.
  OrgWideEmailAddress
  Represents an organization-wide email address for user profiles.
  OutOfOffice
  Represents a user-set value on a profile that shows when the user intends to be out of the office. This object is available in API version 41.0 and later.
  OutgoingEmail
  For internal use only.
  OutgoingEmailRelation
  For internal use only.
  OwnedContentDocument
  Represents a file owned by a user. This object is available in version 30.0 and later.
  OwnerChangeOptionInfo
  Represents default and optional actions that can be performed when a record’s owner is changed. Available in API version 35.0 and later, but to query for change owner metadata, use the OwnerChangeOptionInfo object in Tooling API instead. For more information, see OwnerChangeOptionInfo in the Tooling API.
  PackageInstallEventLog
  PackageInstallEventLog stores details about package installation in the organization. This object is available in API version 62.0 and later.
  PackageLicense
  Represents a license for an installed managed package. This object is available in API version 31.0 and later.
  PackagePushError
  Represents an error encountered during a push request. The number of PackagePushError records created depends on the number of push jobs in the request that result in an error.
  PackagePushJob
  Represents an individual push job for upgrading a package in an org from one version to another version. There can be multiple push jobs created for one push request. For example, if you want to upgrade five orgs as part of one push, you have one PackagePushRequest record and five PackagePushJob records.
  PackagePushRequest
  Represents the push request for upgrading a package in one or many orgs from one version to another version.
  PackageSubscriber
  Represents an installation of a package in an org. This object contains installation information for managed or unlocked packages developed in the org you’re logged in to.
  Participant
  Represents a participant in a ConversationParticipant. An existing or new Participant is referenced each time a new ConversationParticipant is created. This object is available in API version 57.0 and later.
  Partner
  Represents a partner relationship between two Account records or between an Opportunity record and an Account record.
  PartnerFundAllocation
  Represents allocated funds from a partner marketing budget for channel partners. This object is available in API version 41.0 and later.
  PartnerFundClaim
  Represents a claim of funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and later.
  PartnerFundRequest
  Represents a request for funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and later.
  PartnerMarketingBudget
  Represents a budget that provides funds to channel partners for selling and marketing products and services. This object is available in API version 41.0 and later.
  PartnerNetworkConnection
  Represents a Salesforce to Salesforce connection between Salesforce organizations.
  PartnerNetworkRecordConnection
  Represents a record shared between Salesforce organizations using Salesforce to Salesforce.
  PartnerNetworkSyncLog
  Represents the Org Sync Log tab in Salesforce, where Salesforce administrators can track the replication of record inserts and updates being performed in Organization Sync. The Connection Detail page for the replication connection also displays the Org Sync Log’s twenty most recent entries, and provides a link to the log.
  PartnerRole
  Represents a role for an account Partner, such as consultant, supplier, and so on.
  PartyConsent
  Represents consent preferences for an individual. This object is available in API version 48.0 and later.
  Payment
  Represents a single event when a shopper makes a payment. For credit cards, this event is a payment capture or payment sale, but it doesn't appear on the shopper's credit card statement. This object is available in API version 48.0 and later.
  PaymentAuthAdjustment
  Shows information about an adjustment made to an authorized transaction. This object is available in API version 51.0 and later.
  PaymentAuthorization
  Represents a single payment authorization event where users can capture or reverse a payment against a reserve of funds. This object is available in API version 48.0 and later.
  PaymentGateway
  Platform object that represents the connection to an external payment gateway. This object is available in API version 48.0 and later.
  PaymentGatewayLog
  Stores information exchanged between the Salesforce payments platform and external payment gateways. Gateway logs can also record payloads from external payment entities. This object is available in API version 48.0 and later.
  PaymentGatewayProvider
  Setup entity for payment gateways. Defines the connection to a payment gateway Apex adapter. This object is available in API version 48.0 and later.
  PaymentGroup
  Top-level object that groups all payment transactions that are processed for an order or invoice. PaymentGroup is a standalone object, so it isn’t required for users to execute payment transactions (authorizations, captures, refunds, and sales). This object is available in API version 48.0 and later.
  PaymentInitiationSource
  Represents the originating source of a payment. This information helps other Salesforce products integrate with Salesforce Payments. This object is available in API version 63.0 and later.
  PaymentIntent
  Represents data temporarily stored during a transaction’s lifecycle that can identify the buyer, the merchant, and the amount the buyer is sending to the merchant. Data such as timestamp and amount returned can also be stored in PaymentIntent. This object is available in API version 58.0 and later.
  PaymentIntentEvent
  Represents a payment intent platform event. Subscribe to these events so you can listen and respond to them when they’re published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0 and later.
  PaymentLineInvoice
  Represents a payment allocated to or unallocated from an invoice. This object is available in API version 48.0 and later.
  PaymentLink
  A link that a merchant can share with customers to collect payments for products and services. The payment link, which you can embed into a Salesforce app or send directly to a customer, directs the customer to a Pay Now payment page. The page can show a total amount owed or an itemized list or products, shipping and tax charges, and a total amount owed. The customer enters their contact and payment details, and submits their payment. The amounts are shown in the store's currency. This object is available in API version 58.0 and later.
  PaymentLinkEvent
  Represents a payment link platform event. Subscribe to these events so you can listen and respond to them when they’re published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0 and later.
  PaymentMethod
  Represents the method that a buyer uses to compensate the seller of a good or service. Common payment methods include cash, checks, credit or debit cards, money orders, bank transfers, and online payment services. This object is available in API version 48.0 and later.
  PymtSchdDistributionMethod
  Indicates how the total payment is divided into partial payments. This object is available in API version 56.0 and later.
  PaymentScheduleTreatmentDtl
  Contains configuration information for the payment schedule treatment detail. This object is available in API version 56.0 and later.
  PaymentTerm
  Defines your company's method and expectations for receiving payment. This object is available in API version 55.0 and later.
  PaymentTermItem
  Defines the attributes of a payment term that your company uses. The PaymentTermItem is used to determine the due date on invoices. This object is available in API version 55.0 and later.
  PaymentSchedule
  The payment schedule represents a collection of payments that a customer wants to collect at different times for a certain record. A schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each of a schedule’s items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts. When a payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for payment processing if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.
  PaymentScheduleItem
  A payment schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each of a schedule’s items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts. When a payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for payment processing if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.
  PaymentSchedulePolicy
  Contains configuration information for the payment schedule policy. This object is available in API version 56.0 and later.
  PaymentScheduleTreatment
  Contains configuration information for the payment schedule. This object is available in API version 56.0 and later.
  PendingOrderSummary
  Object representing a B2C Commerce order ingested via High Scale Orders before an OrderSummary is created for it. Optimized for online transaction processing (OLTP). This object is available in API version 56.0 and later.
  PendingServiceRouting
  Represents the routing details of a work item that’s waiting to be routed or assigned. This object is available in API version 40.0 and later.
  PendingServiceRoutingInteractionInfo
  Represents PendingServiceRouting interaction information that’s used when work is routed to an agent. For a screen pop, it specifies which records to open when work is routed to an agent from a specific channel. PendingServiceRoutingInteractionInfo is read-only. This object is available in API version 53.0 and later.
  Period
  Represents a fiscal period defined in FiscalYearSettings.
  PermissionSet
  Represents a set of permissions that’s used to grant more access to one or more users without changing their profile or reassigning profiles. This object is available in API version 22.0 and later.
  PermissionSetAssignment
  Represents a user’s assignment to a permission set or permission set group. This object is available in API version 22.0 and later.
  PermissionSetGroup
  Represents a group of permission sets and the permissions within them. Use permission set groups to organize permissions based on job functions or tasks. Then, you can package the groups as needed. This object is available in API version 45.0 and later.
  PermissionSetGroupComponent
  A junction object that relates the PermissionSetGroup and PermissionSet objects via their respective IDs; enables permission set group recalculation to determine the aggregated permissions for the group. This object is available in API version 45.0 and later.
  PermissionSetLicense
  Represents a license that’s used to enable one or more users to receive a specified permission without changing their profile or reassigning profiles. You can use permission set licenses to grant access, but not to deny access. This object is available in API version 29.0 and later.
  PermissionSetLicenseAssign
  Represents the association between a User and a PermissionSetLicense. This object is available in API version 29.0 and later.
  PermissionSetLicenseDefinition (Developer Preview)
  Represents the definition of a custom permission set license, which entitles specified features in a package. This object is available in API version 54.0 and later.
  PermissionSetTabSetting
  Represents a permission set tab setting. Requires the View Setup permission. Use this object to query all tab settings of the permission set. This object is available in API version 45.0 and later.
  PersonAccountOwnerPowerUser
  Represents a user who can own more than 50,000 customer or partner portal accounts. Person account owner power users can own a large number of either customer or partner users. Their role can’t be changed and they must be at the root of the role hierarchy. Person account owner power user objects can't be created if deferred sharing is turned on for your org. Person account owner power user objects can be created while deferred sharing is turned off for an org. Deferred sharing can be turned back on after person account owner power user objects have been created. This object is available in API version 57.0 and later.
  PersonalizationTargetInfo
  Represents a target for an audience. This object is available in API version 47.0 and later.
  PersonTraining
  Represents an assignment of a learning module in Workforce Engagement. This object is available in API version 54.0 and later.
  PicklistValueInfo
  Represents the active picklist values for a given picklist field. This object is available in API version 40.0 and later.
  PickTicket
  A PickTicket represents quantities of one or more products to be picked for fulfillment at a location. It can include products belonging to one or more fulfillment orders. This object is available in API version 57.0 and later.
  PickTicketAssignment
  Represents the association of a FulfillmentOrder with a PickTicket. A PickTicket has one PickTicketAssignment for each FulfillmentOrder containing products to be picked as part of that PickTicket. This object is available in API version 57.0 and later.
  PickTicketProduct
  Represents a quantity of a product to be picked as part of a PickTicket. It can include quantities for multiple FulfillmentOrders. This object is available in API version 57.0 and later.
  PipelineInspectionListView
  Represents a pipeline view or saved filter. A pipeline view shows a set of opportunity records, based on specific criteria. This object is available in API version 53.0 and later.
  PipelineInspectionSumField
  Use this object to learn which field from the opportunity object is used to aggregate Pipeline Inspection metrics on a pipeline view. This object is available in API version 56.0 and later.
  PipelineInspMetricConfig
  Represents the configuration of a forecast category metric that appears in the Pipeline Inspection view. This object is available in API version 55.0 and later.
  PipelineInspMetricConfigLocalization
  Represents the translated label of a Pipeline Inspection metric. This object is available in API version 55.0 and later.
  PlatformAction
  PlatformAction is a virtual read-only object. It enables you to query for actions displayed in the UI, given a user, a context, device format, and a record ID. Examples include standard and custom buttons, quick actions, and productivity actions.
  PlatformEventUsageMetric
  Contains usage data for event publishing and delivery to CometD and Pub/Sub API clients, empApi Lightning components, and event relays. If Enhanced Usage Metrics isn't enabled, usage data is available for the last 24 hours, ending at the last hour, and for historical daily usage. In API 58.0 and later, you can enable Enhanced Usage Metrics to get usage data by event name and client for granular time intervals. PlatformEventUsageMetric contains separate usage metrics for platform events and change data capture events. This object is available in API version 50.0 and later.
  PlatformStatusAlertEvent
  The documentation has moved to PlatformStatusAlertEvent in the Platform Events Developer Guide.
  PortalDelegablePermissionSet
  PortalDelegablePermissionSet is a base platform object used to store permission sets that can be assigned by a delegated portal/external user admin (DPUA) to portal users. This object is available in API version 47.0 and later.
  PresenceConfigDeclineReason
  Represents the settings for a decline reason that a presence user provides when declining work. This object is available in API version 37.0 and later.
  PresenceDeclineReason
  Represents an Omni-Channel decline reason that agents can select when declining work requests. This object is available in API version 37.0 and later.
  PresenceUserConfig
  Represents a configuration that determines a presence user’s settings. This object is available in API version 32.0 and later.
  PresenceUserConfigProfile
  Represents a configuration that determines the settings that are assigned to presence users who are assigned to a specific profile. User-level configurations override profile-level configurations. This object is available in API version 32.0 and later.
  PresenceUserConfigUser
  Represents a configuration that determines the settings that are assigned to a presence user. These user-level configurations override profile-level configurations. This object is available in API version 32.0 and later.
  PriceAdjustmentGroupShape
  Defines the business logic for a top-level price adjustment, for example, a discount applied to an entire order. This object is available in API version 57.0 and later.
  PriceAdjustmentItemShape
  Defines the business logic for an item-level price adjustment, for example, a discount on an order item. This object is available in API version 57.0 and later.
  PriceAdjustmentSchedule
  Represents a series of discounts offered depending on your product's configuration, quantity, and when they’re purchased in combination with other products. This object is available in API version 47.0 and later.
  PriceAdjustmentTier
  Represents a discount tier in a price adjustment schedule. This object is available in API version 47.0 and later.
  Pricebook2
  Represents a price book that contains the list of products that your org sells.
  Pricebook2History
  Represents historical information about changes that have been made to the standard fields of the associated Pricebook2, or to any custom fields with history tracking enabled. This object is available in API version 63.0 and later.
  PricebookEntry
  Represents a product entry (an association between a Pricebook2 and Product2) in a price book.
  PricebookEntryAdjustment
  Read-only junction object created when you associate a price adjustment schedule with a price book entry. This object is available in API version 47.0 and later.
  PrivacyHold
  Represents a Privacy Hold that indicates that a record should be preserved from masking or deletion by Data Management policies in Privacy Center. This object is available in API version 59.0 and later.
  PrivacyHoldReason
  Represents the business or legal purpose for why a record has a Privacy Hold. This object is available in API version 59.0 and later.
  PrivacyJobSession
  Represents the status of past, ongoing, and scheduled policy jobs in Privacy Center. This object is available in API version 59.0 and later.
  PrivacyObjectSession
  Represents the status of each object being processed in past, ongoing, and scheduled policy jobs in Privacy Center. This object is available in API version 59.0 and later.
  PrivacyRequest
  See details and monitor the status of Data Subject Access Requests made in Privacy Center. This object is available in API version 54.0 and later.
  PrivacyRTBFRequest
  Represents a Right to Be Forgotten Request made in Privacy Center. This object is available in API version 59.0 and later.
  PrivacySessionRecordFailure
  Represents error messages encountered during policy job executions in Privacy Center. This object is available in API version 59.0 and later.
  Problem
  Problems represent the root cause data of one or more incidents. This object contains all the details of a problem, documenting the history of the problem from detection to closure. This object is available in API version 53.0 and later.
  ProblemIncident
  Represents a junction object that relates a Problem to an Incident. This object is available in API version 53.0 and later.
  ProblemRelatedItem
  Represents a junction object that relates a Problem to an Asset. This object is available in API version 53.0 and later.
  ProcessDefinition
  Represents the definition of a single approval process.
  ProcessException
  Represents a business exception, such as a processing failure on an order summary. A separate process is required to resolve the failure that caused the process exception before processing can continue. This object is available in API version 50.0 and later.
  ProcessFlowMigration
  Represents a process's migrated criteria and the resulting migrated flow. This object is available in API version 58.0 and later.
  ProcessInstance
  Represents an instance of a single, end-to-end approval process. Use this and the node, step, and workitem process instance objects to create approval history reports.
  ProcessInstanceHistory
  This read-only object shows all steps and pending approval requests associated with an approval process (ProcessInstance).
  ProcessInstanceNode
  Represents a step in an instance of an approval process. Compare to ProcessNode, which describes the step in a process definition. Use this object to retrieve approval history.
  ProcessInstanceStep
  Represents one work item in an approval process (ProcessInstance).
  ProcessInstanceWorkitem
  Represents a user’s pending approval request.
  ProcessNode
  Describes a step in a process definition. Compare to ProcessInstanceNode, which describes a step in a running process. This object is available in API version 31.0 and later.
  ProducerCommission
  Represents a producer's commission for an insurance policy. The commission can be calculated from the commissionable transactions or can be populated from an external system. This object is available in API version 51.0 and later.
  Product2
  Represents a product that your company sells.
  Product2DataTranslation
  Represents the translated values of the data stored within a Product2 record’s fields. This object is available in API version 45.0 and later.
  ProductAttribute
  Represents the attributes that can be associated with a product. This object is available in API version 50.0 and later.
  ProductAttributeSet
  Represents a group of attributes that can be associated with a product. This object is available in API version 50.0 and later.
  ProductAttributeSetItem
  Represents a set of attributes that can be associated with a product. This object is available in API version 50.0 and later.
  ProductAttributeSetProduct
  Represents the product associated with a set of attributes. This object is available in API version 50.0 and later.
  ProductCatalog
  The container that holds a Product Category hierarchy. This object is available in API version 55.0 and later.
  ProductCategory
  Represents the category that products are organized in.This object is available in API version 49.0 and later.
  ProductCategoryProduct
  Holds the relation between product and product category to assign products to a category. This object is available in API version 55.0 and later.
  ProductCategoryDataTranslation
  Represents the translated values for the data stored within a ProductCategory record’s fields. This object is available in API version 46.0 and later.
  ProductComponentGroup
  Represents the logical grouping of associated products in a bundle and the products’ arrangement policy (group cardinality). This object is available in API version 58.0 and later.
  ProductConsumed
  Represents an item from your inventory that was used to complete a work order or work order line item in field service.
  ProductEntitlementTemplate
  Represents predefined terms of customer support (Entitlement) that users can add to products (Product2).
  ProductItem
  Represents the stock of a particular product at a particular location in field service, such as all bolts stored in your main warehouse.
  ProductItemTransaction
  Represents an action taken on a product item in field service. Product item transactions are auto-generated records that help you track when a product item is replenished, consumed, or adjusted.
  ProductMedia
  Represents the rich media, including images and attachments, that can be added to products.This object is available in API version 49.0 and later.
  ProgramProduct
  Represents a junction between Program and Product2. This will hold Product2 values related to a Program. This object is available in API version 58.0 and later.
  ProductQuantityRule
  Represents the relationship between a quantity rule and a product. This object assigns quantity rules to a product. This object is available in API version 51.0 and later.
  ProductRelatedComponent
  Represents a product that is included in a product bundle, a set, or a product and an add-on. This object is available in API version 57.0 and later.
  ProductRelationshipType
  Defines the relationship between two sales transaction items. For example, defines a relationship between a bundle and a bundle component. This object is available in API version 57.0 and later.
  ProductRequest
  Represents an order for a part or parts in field service.
  ProductRequestLineItem
  Represents a request for a part in field service. Product request line items are components of product requests.
  ProductRequired
  Represents a product that is needed to complete a work order or work order line item in field service.
  ProductSellingModel
  Defines one method by which a product can be sold; for example, as a one-time sale, an evergreen subscription, or a term-defined subscription. If the product is sold on subscription, this object defines the subscription’s term. A product can have multiple product selling models. This object is available in API version 55.0 and later.
  ProductSellingModelOption
  A junction object between Product Selling Model and Product2. This object is available in API version 55.0 and later.
  ProductServiceCampaign
  Represents a set of activities to be performed on a product service campaign asset, such as a product recall for safety issues or product defects. This object is available in API version 51.0 and later.
  ProductServiceCampaignItem
  Represents a product service campaign's asset. This object is available in API version 51.0 and later.
  ProductServiceCampaignItemStatus
  Represents a status for a product service campaign item in field service. This object is available in API version 51.0 and later.
  ProductServiceCampaignStatus
  Represents a status for a product service campaign in field service. This object is available in API version 51.0 and later.
  ProductTransfer
  Represents the transfer of inventory between locations in field service.
  ProductWarrantyTerm
  Defines the relationship between a product or product family and warranty term. This object is available in API version 50.0 and later.
  Profile
  Represents a profile, which defines a set of permissions to perform different operations. Operations can include creating a custom profile or querying, adding, updating, or deleting information.
  ProfileSkill
  Represents a profile skill, which describes a user’s professional knowledge. This is a global record for the organization, and users are associated through the ProfileSkillUser object.
  ProfileSkillEndorsement
  Represents a detail relationship of ProfileSkillUser. An endorsement of a profile skill shows approval and support of another user’s publicly declared skill.
  ProfileSkillShare
  Represents a sharing entry on a ProfileSkill.
  ProfileSkillUser
  Represents a detail relationship of User. The object connects profile skills with users.
  Promotion
  Represents a promotion for B2B or D2C stores. This object is available in API version 52.0 and later.
  PromotionLineItemRule
  Lists compound conditions about a promotion. This object is available in API version 59.0 and later.
  PromotionMarketSegment
  Represents a market segment within B2B Commerce that promotions can be assigned to. This object is available in API version 52.0 and later.
  PromotionQualifier
  Represents the product, product category, or order that you want to target with your promotion qualifier in a B2B or D2C store. This object is available in API version 52.0 and later.
  PromotionSegment
  Represents a promotion segment, which you can assign to different stores or buyer groups, allowing them to access the promotion. This object is available in API version 52.0 and later.
  PromotionSegmentBuyerGroup
  Represents a promotion segment, associated with a buyer group, and used for B2B Commerce. This object is available in API version 52.0 and later.
  PromotionSegmentSalesStore
  Represents a promotion segment, associated with a store, and used for B2B Commerce. This object is available in API version 52.0 and later.
  PromotionTarget
  Represents the product, product category, or order that you want to target with your promotion in a B2B Store or D2C store. This object is available in API version 52.0 and later.
  PromotionTier
  Represents a tier of a promotion that includes multiple tiers. A promotion can have up to 10 tiers. This object is available in API version 57.0 and later.
  Prompt
  Represents record details about an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.
  PromptAction
  Represents how the user interacted with the in-app guidance prompt or walkthrough. Available in API version 46.0 and later.
  PromptError
  Represents the error or warning associated with the PromptAction. Available in API version 52.0 and later.
  PromptActionOwnerSharingRule
  Represents a rule which determines PromptAction sharing access for the owners. Available in API version 46.0 and later.
  PromptActionShare
  Represents a sharing entry on a prompt action record. Available in API version 46.0 and later.
  PromptLocalization
  Represents the translated value of a label for record details about in-app guidance when the Translation Workbench is enabled for your org. Available in API version 48.0 and later.
  PromptVersion
  Represents an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.
  PromptVersionLocalization
  Represents the translated value of a label for-app guidance when the Translation Workbench is enabled for your org. Available in API version 48.0 and later.
  ProrationPolicy
  Defines how the price of a subscription is divided into time periods and how the price is calculated for each time period. This object is available in API version 55.0 and later.
  PublicComplaint
  Represents the complaints submitted by public users. This object is available in API version 49.0 and later.
  PurchaseQuantityRule
  Represents a rule that restricts the quantity of a product that can be purchased. The rule can be an increment, minimum, or maximum rule. This object is available in API version 52.0 and later.
  PushTopic
  Represents a query that is the basis for notifying Streaming API clients of changes to records in an org. This object is available in API version 21.0 and later.
  QueueRoutingConfig
  Represents the settings that determine how work items are routed to agents. This object is available in API version 32.0 and later.
  Question
  Represents a question in a zone that users can view and reply to.
  QuestionDataCategorySelection
  A data category selection represents a data category that classifies a question.
  QuestionReportAbuse
  Represents a user-reported abuse on a Question in a Chatter Answers zone. This object is available in API version 24.0 and later.
  QuestionSubscription
  Represents a subscription for a user following a Question. This object is available in API version 24.0 and later.
  QueueSobject
  Represents the mapping between a queue Group and the types associated with the queue, including custom objects.
  QuickText
  This object stores a snippet of text that allows users to send a quick response to a customer. Use quick text to create greetings, answers to common questions, short notes, and more. This object is available in API version 24.0 and later.
  QuickTextUsage
  Represents the usage of quick text on a record, including which quick text was used, who used it, and how they used it. Quick text is a snippet of text that allows users to send a quick response to a customer. This object is available in API version 47.0 and later.
  Quote
  Represents a quote, which is a record showing proposed prices for products and services. Available in API version 18.0 and later.
  QuoteAction
  Indicates the type of sales transaction that’s being quoted; for example, a renewal sale. This object is available in API version 59.0 and later.
  QuoteAdjustmentGroup
  Group containing a set of adjustments applied to a quote. This object is available in API version 58.0 and later.
  QuoteDocument
  Represents a quote in document format. Available in API version 18.0 and later.
  QuoteLineItem
  Represents a quote line item, which is a member of the list of Product2 products associated with a Quote, along with other information about those line items on that quote. Available in API version 18.0 and later.
  QuoteLinePriceAdjustment
  Indicates the calculated price adjustment that is applied to the quote line, for example, a calculated volume discount or the prorated value of a manual discount. Use the quote line price adjustment to inform potential customers about the type, value, and total amount of their discounts. This object is available in API version 56.0 and later.
  QuoteLineRelationship
  Describes the relationship between quote line items, such as items in a bundle. When you create a QuoteLineRelationship object, it’s immutable: it can’t be edited or removed. This object is available in API version 58.0 and later.
  QuoteItemTaxItem
  The tax that is applied to a quote line item. This object is available in API version 55.0 and later.
  RecentFieldChange
  Use this virtual object to see how an opportunity has changed in the past seven days. Learn the previous value of a field, who made the change, and when the change was made. This object is available in API version 52.0 and later.
  RecentlyViewed
  Represents records or list views that the current user has recently viewed or referenced (by viewing a related record). List views are available in API version 29.0 and later.
  Recommendation
  Represents the recommendations surfaced as offers and actions for Einstein Next Best Action. This object is available in API version 45.0 and later.
  RecommendationResponse
  Represents the user responses to a presented offer or recommendation for Einstein Next Best Action. This object is available in API version 51.0 and later.
  RecordAction
  Represents a relationship between a record and an action, such as a flow. Create a RecordAction for every action that you want to associate with a particular record. Available in API version 42.0 and later.
  RecordActionHistory
  Represents the lifecycle of a RecordAction as it goes through different states. Available in API version 44.0 and later.
  RecordsetFilterCriteria
  Represents a set of filters that can be used to match service appointments or assets based on your criteria fields. For example, you can create recordset filter criteria so that only service appointments that satisfy the filter criteria are matched to the filtered shifts, and likewise only maintenance work rules that satisfy your criteria are matched to assets. This object is available in API version 50.0 and later. Assets and maintenance work rules are available in API version 52.0 and later.
  RecordsetFilterCriteriaRule
  Represents a rule using fields from the designated source object to create filters on the filtered, or target, object. RecordsetFilterCriteriaRule is associated with the RecordsetFilterCriteria object. This object is available in API version 50.0 and later.
  RecordsetFltrCritMonitor
  Monitors whether the value of an asset attribute is within the threshold of a recordset filter criteria (RFC). You can monitor one or more RFCs for an Asset. This object is available in API version 57.0 and later.
  RecordType
  Represents a record type.
  RecordTypeLocalization
  Represents the translated value of a label for a record type when the Translation Workbench is enabled for your organization.
  RecordVisibility (Pilot)
  Represents the visibility attributes that determine a record’s read access. This object is read only and is available in API version 46.0 and later.
  RedirectWhitelistUrl
  Represents a trusted URL for external user redirections. Redirections to a different Salesforce org, including its publicly served pages and content, are allowed from your Salesforce org only when the URL is a RedirectWhitelistUrl. For non-Salesforce URLs, a session setting controls whether redirections from pages and components built in Salesforce Classic are restricted to RedirectWhitelistUrl objects. Except for cross-org redirections, you can’t restrict redirections that originate from pages and components built with Lightning Experience. This object is available in API version 48.0 and later.
  Refund
  Represents a refund made against a payment. This object is available in API version 48.0 and later.
  RefundLinePayment
  A refund line that has been applied to a payment. This object is available in API version 48.0 and later.
  RegisteredExternalService
  Represents a registered external service used for checkout integrations by data integrators. This object is available in API version 49.0 and later.
  RelatedListColumnDefinition
  Represents information about a column in a related list. A related list specifies a set of records for a related object, based on specific criteria. This object is available in API version 55.0 and later.
  RelatedListDefinition
  Represents information about a related list. A related list specifies a set of records for a related object, based on specific criteria. This object is available in API version 55.0 and later.
  RemoteKeyCalloutEvent
  The documentation has moved to RemoteKeyCalloutEvent in the Platform Events Developer Guide.
  Reply
  Represents a reply that a user has submitted to a question in an answers zone.
  ReplyReportAbuse
  Represents a user-reported abuse on a Reply in a Chatter Answers zone. This object is available in API version 24.0 and later.
  ReplyText
  A text reply generated by Einstein Reply Recommendations that is based on closed chat transcripts. Admins review replies and publish them to quick text, editing them as needed. Einstein recommends relevant published replies to support agents in the Lightning Service Console, and agents can insert replies into chats or messaging sessions. This object is available in API version 49.0 and later.
  Report
  Represents a report, a set of data that meets certain criteria, displayed in an organized way. Access is read-only. This object is available in API version 20.0 and later.
  ReportEventLog
  Report event logs contain information about what happened when a user ran a report. This event type includes all activity that's in the Report Export event type, and additional information. For example, it has user activity for reports exported as both Formatted Report and Details Only output. This object is available in API version 55.0 and later.
  ReportTag
  Associates a word or short phrase with a Report. This object is available in API version 20.0 and later.
  ReputationLevel
  Represents a reputation level defined for an Experience Cloud site. This object is available in API version 32.0 and later.
  ReputationLevelLocalization
  Represents the translated value of a reputation level. Reputation level localization only applies for reputation levels in Experience Cloud sites. This object is available in API version 35.0 and later.
  ReputationPointsRule
  Represents the reputation point rules for an Experience Cloud site. Each rule specifies an action that members can earn points from and the points associated with those actions in a particular site. This object is available in API version 32.0 and later.
  ResourceAbsence
  Represents a time period in which a service resource is unavailable to work in Field Service, Salesforce Scheduler, or Workforce Engagement. This object is available in API version 38.0 and later.
  ResourcePreference
  Represents an account’s preference for a specified service resource on field service work.
  RestApiEventLog
  REST API event logs contain details about REST-specific requests. This object is available in API version 55.0 and later.
  ReturnOrder
  Represents the return or repair of inventory or products in Field Service, or the return of order products in Order Management. This object is available in API version 42.0 and later.
  ReturnOrderItemAdjustment
  Represents a price adjustment on a return order line item. This object is available in API version 50.0 and later.
  ReturnOrderItemTax
  Represents the tax on a return order line item or return order item adjustment. This object is available in API version 50.0 and later.
  ReturnOrderLineItem
  Represents a specific product that is returned or repaired as part of a return order in Field service, or a specific order item that is returned as part of a return order in Order Management. This object is available in API version 42.0 and later.
  ReturnOrderOwnerSharingRule
  Represents the rules for sharing a return order with user records other than the owner or anyone above the owner in the role hierarchy. This object is available in API version 42.0 and later.
  RevenueAsyncOperation
  Represents the status of an asynchronous process initiated by a REST request in Subscription Management. This object is available in API versions 57.0 to 59.0. Use AsyncOperationTracker instead of RevenueSyncOperation in API version 59.0 and later.
  RevenueTransactionErrorLog
  Contains information about errors that occurred while processing a request. The error record persists until another error with the same category, primary record, and (optionally) related record occurs. This object is available in API version 55.0 and later.
  RpaFlowResultEvent
  Reserved for future use.
  RpaRobot
  Reserved for future use.
  RpaRobotAsgnMaintWindow
  Reserved for future use.
  RpaRobotAsgnSessionInf
  Reserved for future use.
  RpaRobotDefinition
  Reserved for future use.
  RpaRobotMaintWindow
  Reserved for future use.
  RpaRobotMaintWindowDef
  Reserved for future use.
  RpaRobotPool
  Reserved for future use.
  RpaRobotPoolAsgnRobot
  Reserved for future use.
  RpaRobotPoolDefinition
  Reserved for future use.
  RpaRobotPoolFlowAsgn
  Reserved for future use.
  RpaRobotSessionInfo
  Reserved for future use.
  RpaRobotSessionInfoDef
  Reserved for future use.
  RuleTerritory2Association
  Represents a record-assignment rule and its association to an object, such as Account. Available if Sales Territories has been enabled.
  SalesAIScoreCycle
  Represents the cycle type and ID used to score records. This object is available in API version 47.0 and later.
  SalesAIScoreModelFactor
  Represents the factors that Sales Cloud Einstein uses to build a scoring model. Scoring models are used by features, such as Opportunity Scoring, to score individual records. This object is available in API version 47.0 and later.
  SalesChannel
  Represents the origin of an order. For example, a web storefront, physical store, marketplace, or mobile app. If you integrate Salesforce Order Management with Salesforce B2C Commerce, set up a SalesChannel corresponding to each Site in your B2C Commerce implementation. This object is available in API version 48.0 and later.
  SalesforceContract
  Read-only virtual object used in the Your Account App. Represents contract information related to your organization’s Salesforce subscription.
  SalesforceInvoice
  Read-only virtual object used in the Your Account App. Represents information about your organization’s invoices with Salesforce.
  SalesforcePayment
  Read-only virtual object used in the Your Account App. Represents information about payments related to your organization’s Salesforce invoice.
  SalesforceQuote
  Read-only virtual object used in the Your Account App. Represents information about your organization’s quotes with Salesforce.
  SalesStoreCatalog
  Represents the catalog associated with a store. This object is available in API version 49.0 and later.
  SalesTransactionItemShape
  Defines the business logic for a sales transaction shape item, for example, an item in an order. This object is available in API version 57.0 and later.
  SalesTransactionShape
  Defines the business logic for a sales transaction; for example, an order, a quote, or a cart. This object is available in API version 57.0 and later.
  SalesTrxnItemRelationShape
  Describes the relationship between sales transaction shape items; for example, a bundle or set. This object is available in API version 57.0 and later.
  SalesTrxnItemRelationship
  Describes the relationship between sales transaction items; for example, a bundle or set. This object interface is available in API version 58.0 and later.
  SalesWorkQueueSettings
  Represents settings used to customize work queue options for third-party scoring. Third-party scoring enables custom number fields on person accounts, contacts, and leads. You must be a Sales Engagement customer to update this object. Previously, you could only use the Einstein Intelligence Score for third-party scoring. Available starting in Version 47.0.
  SandboxStatusEventLog
  SandboxStatusEventLog stores details about Sandbox copies. This object is available in API version 62.0 and later.
  SamlSsoConfig
  Represents a SAML Single Sign-On configuration.This object is available in API version 32.0 and later.
  SavedPaymentMethod
  Represents a payment method saved by an authenticated customer. This object is available in API version 58.0 and later
  SavedPaymentMethodEvent
  Represents a saved payment method platform event. Subscribe to these events so you can listen and respond to them when they’re published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0 and later.
  SchedulingAdherenceDetail
  Represents the breakdown of daily shift adherence data by agent status. This object is available in API version 54.0 and later.
  SchedulingAdherenceSummary
  Represents daily shift adherence data for a service resource in a service territory and job profile on a specific date. This object is available in API version 54.0 and later.
  SchedulingConstraint
  Represents scheduling constraints on each service resource. This object is available in API version 50.0 and later.
  SchedulingObjective
  Represents business goals that the scheduling tools consider. This object is available in API version 53.0 and later.
  SchedulingRule
  Represents scheduling rules that are hard constraints in the scheduling logic engine. This object is available in API version 52.0 and later.
  SchedulingRuleParameter
  Represents scheduling rule parameters associated with a scheduling rule. This object is available in API version 52.0 and later.
  Scontrol
  A custom s-control, which is custom content that is hosted by the system but executed by the client application.
  ScontrolLocalization
  The translated value of the field label for an s-control.
  Scorecard
  Use scorecards to measure partner performance and establish benchmarks for channel programs within Experience Cloud. Display any report summary results that your channel account manager or executive team wants to see. This object is available in API version 40.0 and later.
  ScorecardAssociation
  Represents a connection between a specific scorecard and the associated account, channel program, or channel program level. This object is available in API version 41.0 and later.
  ScorecardMetric
  Stores information about a Salesforce report that is run and summarized to get a single value. The stored value is added as a metric to the related Scorecard object. This object is available in API version 40.0 and later.
  ScratchOrgInfo
  Represents a scratch org and its audit log. Use this object to create a scratch org and keep a log of its creation and deletion. This object is available in API version 41.0 and later.
  SearchActivity
  Represents search activity on a Knowledge article. Also known as KnowledgeSearchActivity. This object is available in API version 38.0 and later.
  SearchClickEventLog
  Search Click Event Log contains details about the user’s interaction with the search results. This object is available in API version 61.0 and later.
  SearchEventLog
  Search Event Log provides details about the user’s search query. This object is available in API version 61.0 and later.
  SearchPromotionRule
  Represents a promoted search term, which is one or more keywords that you associate with a Salesforce Knowledge article. When a user’s search query includes these keywords, the associated article is returned first in search results. This object is available in API version 31.0 and later.
  SecurityCustomBaseline
  Provides the ability to read, create, and delete user-defined custom security baselines, which define an org’s security standards. This object is available in API version 39.0 and later.
  SelfServiceUser
  Represents a Contact who has been enabled to use your organization’s Self-Service portal, where he or she can obtain online support.
  Seller
  Represents the seller role of an individual with respect to a particular company or organization. This object is available in API version 53.0 and later.
  ServiceAppointment
  Represents an appointment to complete work for a customer in Field Service, Lightning Scheduler,Intelligent Appointment Management, and Virtual Care.This object is available in API version 38.0 and later.
  ServiceAppointmentStatus
  Represents a possible status of a service appointment in field service.
  ServiceChannel
  Represents a channel of work items that are received from your organization—for example, cases, chats, or leads. This object is available in API version 32.0 and later.
  ServiceChannelFieldPriority
  Represents a secondary routing priority field-value mapping. This object is available in API version 47.0 and later.
  ServiceChannelStatus
  Represents the status that’s associated with a specific service channel. This object is available in API version 32.0 and later.
  ServiceChannelStatusField
  Represents the values that you use to indicate completed and in-progress work item status for the status field in the Status-Based Capacity routing model. This object is available in API version 49.0 and later.
  ServiceContract
  Represents a customer support contract (business agreement). This object is available in API version 18.0 and later.
  ServiceContractOwnerSharingRule
  Represents the rules for sharing a ServiceContract (customer service agreement) with users other than the owner. This object is available in API version 18.0 and later.
  ServiceCrew
  Represents a group of service resources who can be assigned to service appointments as a unit.
  ServiceCrewMember
  Represents a technician service resource that belongs to a service crew.
  ServiceCrewOwnerSharingRule
  Represents the rules for sharing a service crew with user records other than the owner or anyone above the owner in the role hierarchy.
  ServicePresenceStatus
  Represents a presence status that can be assigned to a service channel. This object is available in API version 32.0 and later.
  ServiceReport
  Represents a report that summarizes a work order, work order line item, or service appointment.
  ServiceReportLayout
  Represents a service report template in field service.
  ServiceResource
  Represents a service technician or service crew in Field Service and Salesforce Scheduler, or an agent in Workforce Engagement. This object is available in API version 38.0 and later.
  ServiceResourceCapacity
  Represents the maximum number of scheduled hours or number of service appointments that a capacity-based service resource can complete within a specific time period. This object is available in API version 38.0 and later.
  ServiceResourceCapacityHistory
  Represents the history of changes made to tracked fields on a service resource capacity record. This object is available in API version 38.0 and later.
  ServiceResourceDataTranslation
  Represents the translated values of the data stored within a ServiceResource record’s fields. This object is available in API version 54.0 and later.
  ServiceResourceOwnerSharingRule
  Represents the rules for sharing a service resource with user records other than the owner or anyone above the owner in the role hierarchy. This object is available in API version 38.0 and later.
  ServiceResourcePreference
  Represents the service resource scheduling preferences that are considered as a business objective in the scheduling logic engine. This object is available in API version 52.0 and later.
  ServiceResourceSkill
  Represents a skill that a service resource possesses in Field Service and Lightning Scheduler. This object is available in API version 38.0 and later.
  ServiceSetupProvisioning
  Represents a task completed by the Service Setup Assistant. This object is available in API version 52.0 and later.
  ServiceTerritory
  Represents a geographic or functional region in which work can be performed in Field Service, Salesforce Scheduler, or Workforce Engagement. This object is available in API version 38.0 and later.
  ServiceTerritoryDataTranslation
  Represents the translated values of the data stored within a ServiceTerritory record’s fields. This object is available in API version 54.0 and later.
  ServiceTerritoryLocation
  Represents a location associated with a particular service territory in field service.
  ServiceTerritoryMember
  Represents a service resource who can be assigned in a service territory in Field Service, Salesforce Scheduler, or Workforce Engagement. This object is available in API version 38.0 and later.
  ServiceTerritoryWorkType
  Represents the relationship between a ServiceTerritory object and a WorkType object for Salesforce Scheduler appointments. This object is available in API version 45.0 and later.
  SessionPermSetActivation
  The SessionPermSetActivation object represents a permission set assignment activated during an individual user session. When a SessionPermSetActivation object is inserted into a permission set, an activation event fires, allowing the permission settings to apply to the user’s specific session. This object is available in API versions 37.0 and later.
  SetupAssistantStep
  For internal use only.
  SetupAuditTrail
  Represents changes you or other admins made in your org’s Setup area for at least the last 180 days. This object is available in API version 15.0 and later.
  SetupEntityAccess
  Represents the enabled setup entity access settings (such as for Apex classes) for the parent PermissionSet. This object is available in API version 25.0 and later.
  ShapeRepresentation
  Contains information about the shape of an org. The shape of an org includes licenses and limits information. You can easily create scratch orgs based on a source org’s shape. This object is available in API version 50.0 and later.
  SharingRecordCollection
  Represents a collection of records. This object is available in API version 51.0 and later.
  SharingRecordCollectionItem
  Represents a single record in a collection of records. This object is available in API version 51.0 and later.
  SharingRecordCollectionMember
  Represents a user with access to a collection of records. This object is available in API version 51.0 and later.
  Shift
  Represents a shift for service resource scheduling. Available in API versions 46.0 and later.
  ShiftHistory
  Represents the history of changes made to tracked fields on a time sheet. Available in API versions 46.0 and later.
  ShiftOwnerSharingRule
  Represents the rules for sharing a shift with user records other than the owner or anyone above the owner in the role hierarchy. Available in API versions 46.0 and later.
  ShiftPattern
  Represents a pattern of templates for creating shifts. This object is available in API version 51.0 and later.
  ShiftPatternEntry
  ShiftPatternEntry links a shift template to a shift pattern. This object is available in API version 51.0 and later.
  ShiftSegment
  Represents a scheduled activity within a shift. This object is available in API version 55.0 and later.
  ShiftSegmentType
  Represents a type of activity scheduled within a shift. This object is available in API version 55.0 and later.
  ShiftShare
  Represents a sharing entry on a field service shift. Available in API versions 46.0 and later.
  ShiftStatus
  Represents a shift, such as Tentative, Published, or Confirmed. Available in API versions 46.0 and later.
  ShiftTemplate
  Represents a template for creating shifts. This object is available in API version 51.0 and later.
  Shipment
  Represents the transport of inventory in field service or a shipment of order items in Order Management.
  ShipmentItem
  Represents an order item included in a shipment. This object is available in API version 51.0 and later.
  ShippingCarrier
  Shipping company or carrier responsible for transporting goods or packages. Examples include UPS, FedEx, and USPS. This object is available in API version 61.0 and later.
  ShippingCarrierMethod
  Shipping service provided by a shipping carrier. Examples include Ground, 2Day, and NextDay. Service depends on the range of transit times available for each carrier. This object is available in API version 61.0 and later.
  ShippingConfigurationSet
  Shipping configuration for a set of products in a store. This object is available in API version 59.0 and later.
  ShippingRateArea
  A designated geographical area that’s available for shipping. This object is available in API version 59.0 and later.
  ShippingRateGroup
  Available shipping rates based on shipping destination. This object is available in API version 59.0 and later.
  SignupRequest
  Represents a request for a new sign-up. SignupRequest isn’t supported in sandbox instances and will result in an error. This object is available in API version 27.0 and later.
  Site
  Represents a public website that is integrated with an org. This object is available in API version 16.0 and later.
  SiteDetail
  Represents the details of a Salesforce site or Experience Cloud site. Available in API Version 38.0 and later.
  SiteDomain
  SiteDomain is a read-only object, and a one-to-many replacement for the Site.TopLevelDomain field. This object is available in API version 21.0, and has been deprecated as of API version 26.0. In API version 26.0 and later, use the Domain and DomainSite objects instead.
  SiteHistory
  Represents the history of changes to the values in the fields of a site. This object is generally available in API version 18.0 and later.
  SiteIframeWhitelistUrl
  Represents a list of external domains that you allow to frame your Salesforce site or Experience Cloud site pages. This object is available in API version 44.0 and later.
  SiteRedirectMapping
  Represents a site redirect from an external site to an Experience Cloud site. This object is available in API version 52.0 and later.
  Skill
  Represents a category or group of Chat users or service resources in Field Service or Workforce Engagement. This object is available in API version 24.0 and later.
  SkillLevelDefinition
  Represents a skill which can be acquired by completing enablement site (myTrailhead) modules. This object is available in API version 51.0 and later.
  SkillLevelProgress
  Represents training progress for a given user. This object is available in API version 51.0 and later.
  SkillProfile
  Represents a join between Skill and Profile. This object is available in API version 24.0 and later.
  SkillRequirement
  Represents a skill that is required to complete a particular task in Field Service, Omni-Channel, Salesforce Scheduler, or Workforce Engagement. Skill requirements can be added to pending service routing objects in Omni-Channel. They can be added to work types, work orders, and work order line items in Field Service and Lightning Scheduler. And they can be added to job profiles in Workforce Engagement. This object is available in API version 38.0 and later. You also can add skill requirements to work items in Omni-Channel skills-based routing using API version 42.0 and later.
  SkillUser
  Represents a join between Skill and User. This object is available in API version 24.0 and later.
  SlaProcess
  Represents an entitlement process associated with an Entitlement. This object is available in API version 19.0 and later.
  Snippet
  Represents a snippet, which is a container for rich text that can be reused across Account Engagement emails and email templates. This object is available in API version 47.0 and later.
  SnippetAssignment
  Represents a relationship between a snippet and a campaign. Assignments are required to use snippet content in Account Engagement emails and email templates. A snippet can be assigned to more than one campaign. This object is available in API version 47.0 and later.
  SoapApiEventLog
  SOAP API events contain details about your org's SOAP API request activity. This object is available in API version 55.0 and later.
  SocialPersona
  Represents a snapshot of a contact's profile on a social network such as Facebook or Twitter. This object is available in API version 22.0 and later.
  SocialPost
  Represents a snapshot of a post on a social network such as a Facebook or Twitter. This object is available in API version 23.0 and later.
  Solution
  Represents a detailed description of a customer issue and the resolution of that issue.
  SolutionStatus
  Represents the status of a Solution, such as Draft, Reviewed, and so on.
  SolutionTag
  Associates a word or short phrase with a Solution.
  SOSDeployment
  Represents the general settings for deploying SOS video call capability in a native mobile application. This object is available in API version 34.0 and later.
  SOSSession
  This object is automatically created for each SOS session and stores information about the session. This object is available in API versions 34.0 and later.
  SOSSessionActivity
  Captures information about specific events that occur during an SOS video call, such as when an SOS call begins or ends. This object is available in API version 34.0 and later.
  Stamp
  Represents a User Specialty. This object is available in API version 39.0 and later.
  StampAssignment
  Represents assignment of a User Specialty to a user. This object is available in API version 39.0 and later.
  StandardInvocableActionType
  Represents a collection of fields to set up granular user permissions for access to a standard invocable action in Flow Builder. This object is available in API version 60.0 and later.
  StandardShippingRate
  Standard shipping rate for a store. This object is available in API version 59.0 and later.
  StaticResource
  Represents a static resource that can be used in Visualforce markup.
  StoreIntegratedService
  Represents an association between an integration and a store. This object is available in API version 49.0 and later.
  StreamingChannel
  Represents a channel that is the basis for notifying listeners of generic Streaming API events. This object is available in API version 29.0 and later.
  Salesforce Surveys Object Model
  Learn about how Salesforce Surveys objects relate to one another in Salesforce.
  Survey
  Represents a survey.
  SurveyEmailBranding
  Represents the configuration settings for invitation emails sent to survey participants for a particular survey.
  SurveyEngagementContext
  Represents the context based on which a survey invitation was sent or a survey response was received. This object is available in API version 49.0 and later.
  SurveyInvitation
  Represents the invitation sent to a participant to complete the survey.
  SurveyPage
  Represents a page, such as the title page or a question page, in a survey.
  SurveyQuestion
  Represents a question in a survey.
  SurveyQuestionChoice
  Represents an answer choice that a participant can select for a survey question.
  SurveyQuestionResponse
  Represents a participant’s answer to a specific question.
  SurveyQuestionScore
  Represents the aggregate of responses for the following question types: date, multiple choice, picklist, radio, ranking, rating, scoring, slider, and Net Promoter Score® (NPS®).
  SurveyResponse
  Represents information about a participant’s response to a survey, such as the status of the response, the participant’s location, and when the survey was completed.
  SurveySubject
  Represents a relationship between a survey and another object, such as an account or a case.
  SurveyVersion
  Represents a version of a survey.
  SurveyVersionAddlInfo
  Represents additional information about a survey version. This information defines the default settings of a survey version. This object is available in API version 49.0 and later.
  SvcCatalogCategory
  Represents a group of Service Catalog items by functional area. This object is available in API version 58.0 and later.
  SvcCatalogCategoryItem
  Represents an association between a Service Catalog item and category. Service catalog items can be grouped into categories. This object is available in API version 58.0 and later.
  SvcCatalogFilterCriteria
  Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item. This object is available in API version 60.0 and later.
  SvcCatalogItemDef
  Represents a service catalog item that can be requested by a service catalog user. This object is available in API version 53.0 and later.
  SvcCatalogRequest
  Represents a request made by a user using the Service Catalog. Catalog builders use this object to report on Service Catalog activity. This object is available in API version 53.0 and later.
  SvcCatalogReqRelatedItem
  Represents an item related to a Service Catalog Request. This object is available in API version 53.0 and later.
  Swarm
  Represents a team of agents, Salesforce users, or Slack users in a Slack channel or thread dedicated to solving a problem. This problem can be related to a support case, incident, sales opportunity, or change request. This object is available in API version 55.0 and later.
  SwarmMember
  Represents a Salesforce member, such as an agent, of a swarm. This object is available in API version 55.0 and later.
  TabDefinition
  Represents a custom tab. Returns only the tabs that the current user has access to. This object is available in API version 43.0 and later.
  TagDefinition
  Defines the attributes of child Tag objects.
  Task
  Represents a business activity such as making a phone call or other to-do items. In the user interface, Task and Event records are collectively referred to as activities.
  TaskPriority
  Represents the importance or urgency of a task, such as High, Normal, or Low.
  TaskRelation
  Represents the relationship between a task and a lead, contacts, and other objects related to the task. If Shared Activities is enabled, this object doesn’t support triggers, workflow, or data validation rules. This object is available in API version 24.0 and later.
  TaskStatus
  Represents the status of a task, such as Not Started, Completed, or Closed.
  TaskTag
  Associates a word or short phrase with a task .
  TaskWhoRelation
  Represents the relationship between a task and a lead or contacts. This object is available in API version 29.0 and later.
  TaxEngine
  A tax engine represents both an instance of a tax engine provider as well as the merchant credentials for that specific instance. When Subscription Management calculates tax on an order item, it sends a request through Subscription Management Tax Calculation API to an external tax engine. The Salesforce tax engine record contains information passed to the external tax engine, such as This object is available in API version 55.0 and later.
  TaxEngineInteractionLog
  A record of a communication with an external tax engine following a tax calculation request. This object is available in API version 55.0 and later.
  TaxEngineProvider
  Represents general information about a service that manages a tax engine, such as the ID of the tax adapter Apex class in Salesforce, and the engine’s namespace prefix. Tax engine providers have a one-to-many relationship with tax engines, where the tax engine record represents a specific configuration of a tax engine that can be assigned to multiple order items. This object is available in API version 55.0 and later.
  TaxGeoConfig
  Represents a tax configuration associated with a GeoCountry. This object is available in API version 57.0 and later.
  TaxPolicy
  A tax policy contains a group of tax treatments, where each treatment represents parameters to determine how a particular product is taxed for a transaction line item. Tax policies are related to products, which pass the policy on to the resulting order items. When you activate an order, Subscription Management assigns a tax treatment to each order item based on the tax policy's DefaultTaxTreatmentId, then uses the tax treatment to calculate tax. This object is available in API version 55.0 and later.
  TaxRate
  Represents a tax rate for a tax code and country. This object is available in API version 56.0 and later.
  TaxTreatment
  A tax treatment contains details about how Salesforce and external engines calculate taxes, and the tax engine to use for tax calculation. The IsTaxable field determines whether tax is calculated for the product in the transaction. The tax code, tax engine, and product code are sent via API to the external tax calculation service. When you invoice an order item that has a tax treatment, the invoice line inherits the tax treatment from the order item’s related billing schedule. The invoice line’s TaxCode field is populated based on the code that the tax engine used for calculation. This object is available in API version 55.0 and later.
  TenantSecret
  This object stores an encrypted organization-specific key fragment that’s used with the primary secret (KDF seed) to produce org-specific data encryption keys. This object is available in API version 34.0 and later.
  TenantSecurityAlertRuleSelectedTenant
  Stores information about a Security Center alert rule for tenants. This object is available for Security Center subscribers in API version 55.0 and later.
  TenantSecurityApiAnomaly
  Stores detected anomalies in how users typically make API calls. Fore more information, see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityCertificate
  Stores metric details related to public key certificate information. The certificate binds the public key to the identity of an entity. This object is available in API version 63.0 and later.
  TenantSecurityConnectedApp
  Stores the details for a connected app that was added to or removed from a Security Center tenant. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityCredentialStuffing
  Stores when a user successfully logs in to Salesforce during an identified credential stuffing attack. For more information, see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityCustomMetricSetup
  Represents the configuration for a custom metric within Security Center. This object is available in API version 61.0 and later.
  TenantSecurityCustomMetricDetail
  Stores TenantSecurityCustomMetricStat drill down details. This object is available in API version 62.0 and later.
  TenantSecurityCustomMetricStat
  Represents custom metric data within Security Center. This object is available in API version 61.0 and later.
  TenantSecurityEncryptedField
  Represents fields encrypted under your Shield Platform Encryption policy. This object is available in API version 61.0 and later.
  TenantSecurityGuestUserAnomaly
  Represents metric details for guest user anomaly events detected by Threat Detection. This object is available in API version 60.0 and later.
  TenantSecurityEncryptionPolicy
  Stores tenant encryption policy status. This object is available in API version 58.0 and later.
  TenantSecurityFeature
  Stores org features across all tenants in Security Center. This object is available in API version 57.0 and later.
  TenantSecurityHealthCheckBaselineTrend
  Stores metric details related to Health Check baseline settings. The Health Check detail page in Security Center displays scores and settings for all your tenants in one place. Use this object to get details about which metrics are collected and for which tenants, and changes made to the Health Check baseline. This object is available to Security Center subscribers in API version 54.0 and later.
  TenantSecurityHealthCheckDetail
  Stores the details of Health Check scores for a connected tenant. The Health Check detail page in Security Center displays scores and settings for all your tenants in one place. Use this object to get settings and risks per tenant on a selected date. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityHealthCheckTrend
  Stores the history of Security Health Check scores for a connected tenant within Security Center. Health Check in Security Center displays Health Check scores and the average risk settings for all your tenants in one place. This object belongs to the parent tenant and stores Health Check data pushed from child tenants. This object is available for Security Center subscribers in API version 53.0 and later.
  TenantSecurityLicense
  Stores license usage information within Security Center. This object is available in API version 59.0 and later.
  TenantSecurityLogin
  Stores the login details of a single user to a tenant, grouped by date and type. You can query this object to find out how many times the user logged in to a specific tenant using a specific login type (for example, username/password or SSO). This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityLoginIpRangeTrend
  Stores details of changes related to login IP ranges in Security Center. This object is available in API version 59.0 and later.
  TenantSecurityMobilePolicyTrend
  Stores metrics related to changes in mobile security policies across all tenants in Security Center. This object is available to Security Center subscribers in API version 54.0 and later.
  TenantSecurityMonitorMetric
  Stores the daily count and daily count change for a metric within Security Center. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityNotification
  Stores information about notifications that were triggered in Security Center as a function of the Alerts feature. For more information, see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 54.0 and later.
  TenantSecurityNotificationRule
  Stores an alert configured in the Security Center Alerts feature to notify recipients of changes made to security settings. For more information, see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityMetricDetailLink
  Represents the link between the metric count and metric drill down. This object is available in API version 48.0 and later.
  TenantSecurityPackage
  Stores details about managed and unmanaged packages that are added, updated, or removed from a tenant in Security Center. Use this object to identify whether new packages are installed, upgraded, or uninstalled from your connected tenants. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityPolicy
  Stores security policies created and deployed in Security Center. For more information, see Define and Deploy Security Policies. This object is available to Security Center subscribers in API version 54.0 and later.
  TenantSecurityPolicyDeployment
  Stores the status of deployments of a Security Center policy on a tenant. For more information, see Define and Deploy Security Policies. This object is available to Security Center subscribers in API version 54.0 and later.
  TenantSecurityPolicySelectedTenant
  Stores the list of tenants selected for a Security Center policy. For more information, see Define and Deploy Security Policies. This object is available to Security Center subscribers in API version 54.0 and later.
  TenantSecurityReportAnomaly
  Stores anomalies in how users run or export reports, including unsaved reports, as detected by Threat Detection. For more information, see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecuritySessionHijacking
  Stores information about session hijacking events as detected by Threat Detection within connected tenants in Security Center. For more information, see Threat Detection. This object is available for Security Center subscribers in API version 53.0 and later.
  TenantSecurityTenantInfo
  Stores information on changes related to the tenant history. This object is available in API version 56.0 and later.
  TenantSecurityTransactionPolicyTrend
  Stores changes to the count of Transaction Security Policies for a connected tenant within Security Center. This object is available for Security Center subscribers in API version 55.0 and later.
  TenantSecurityTrigTransactionSecurityPol
  Stores metric details related to Transaction Security Policy triggering events. This object is available in API version 63.0 and later.
  TenantSecurityTrustedIpRangeTrend
  Stores details of changes related to trusted IP ranges in Security Center.This object is available for Security Center subscribers in API version 54.0 and later.
  TenantSecurityUserActivity
  Stores details related to how a user interacts with a tenant. Use this object to determine whether to reevaluate a user’s access to your org for security purposes. You can check whether a user has never logged in, hasn’t been active for 90 days, has a frozen account, or isn’t using multi-factor authentication. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantSecurityUserPerm
  Stores information on permissions assigned to a user. Use this object to see which tenants a user is assigned to. This object is available to Security Center subscribers in API version 53.0 and later.
  TenantUsageEntitlement
  Represents a data structure that contains information about the features or functionalities that a Salesforce org has access to. This object is available in API version 28.0 and later.
  Territory
  Represents a flexible collection of accounts and users where the users have at least read access to the accounts, regardless of who owns the accounts. Available if Sales Territories has been enabled.
  TerritoryMgmtObjectConfig
  Represents territory management settings and defaults for a particular object. This object is available in API version 56.0 and later.
  Territory2
  Represents a sales territory. Available if Sales Territories has been enabled.
  Territory2AlignmentLog
  Represents the start and end status of a territory assignment rule run job. This object is available in API version 54.0 and later.
  Territory2Model
  Represents a territory model. Available if Sales Territories has been enabled.
  Territory2ModelHistory
  Represents the history of changes to the values in the fields on a territory model. Available if Sales Territories has been enabled.
  Territory2ObjectExclusion
  Represents the objects that aren’t included in territory assignment rule runs, even when they meet assignment rule criteria. This object is available in API version 54.0 and later.
  Territory2ObjSharingConfig
  Represents the sharing access level of objects assigned to a particular territory. This object is available in API version 56.0 and later.
  Territory2Type
  Represents a category for territories (Territory2). Every Territory2 must have a Territory2Type. Available only if Sales Territories has been enabled for your organization.
  TerritoryAdminAssignment
  Represents designated team members who can administer specific territories and their descendants. This object is available in API version 63.0 and later.
  TestSuiteMembership
  Associates an Apex class with an ApexTestSuite. This object is available in API version 36.0 and later.
  ThirdPartyAccountLink
  Represents the list of external users who authenticated using an authentication provider. This object is available in API version 32.0 and later.
  ThreatDetectionFeedback
  Represents feedback provided by a user about a Threat Detection event that occurred in your org. The feedback specifies whether the event was malicious, suspicious, not a threat, or unknown. Each ThreatDetectionFeedback object is associated with one of these Threat Detection storage events: ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore, or SessionHijackingEventStore. This object is available in API version 49.0 and later.
  TimeSheet
  Represents a schedule of a service resource’s time in Field Service or Workforce Engagement. This object is available in API v47.0 and later.
  TimeSheetEntry
  Represents a span of time that a service resource spends on a field service task. This object is available in API version 47.0 and later.
  TimeSlot
  Represents a period of time on a specified day of the week during which work can be performed in Field Service, Salesforce Scheduler, or Workforce Engagement. Operating hours consist of one or more time slots. This object is available in API version 38.0 and later.
  TimeSlotHistory
  Represents the history of changes made to tracked fields on a time slot. This object is available in API version 38.0 and later.
  Topic
  Represents a topic on a Chatter post or record. This object is available in API version 28.0 and later.
  TopicAssignment
  Represents the assignment of a topic to a specific feed item, record, or file. This object is available in API version 28.0 and later.
  TopicLocalization
  Represents the translated version of a topic name. Topic localization applies only to navigational and featured topics in Experience Cloud sites. This object is available in API version 33.0 and later.
  TopicUserEvent
  Represents an action (such as comment, post, like, or share) made by a user on a topic. This object is available in API version 42.0 and later.
  TransactionSecurityPolicy
  Represents a transaction security policy definition.
  TransactionSecurityEventLog
  Transaction Security event logs contain details about policy execution. Legacy transaction security policy details are supported in API version 38.0 and later. Enhanced transaction security policy details are supported in API version 55.0 and later.
  Translation
  The Translation object represents the languages enabled for translation in your Salesforce org. This object is available in API version 47.0 and later.
  TravelMode
  Represents a travel mode used for travel time calculations. The records include information about the type of transportation (such as Car or Walking), whether a vehicle can take toll roads, and whether a vehicle is transporting hazardous materials. This object is available in API version 54.0 and later.
  TwoFactorInfo
  Stores a user’s secret for multi-factor operations. Use this object when customizing multi-factor authentication in your organization. (Note that multi-factor authentication was formerly called two-factor authentication.) This object is available in API version 32.0 and later.
  TwoFactorMethodsInfo
  Stores information about which identity verification methods a user has registered. This object is available in API version 37.0 and later.
  TwoFactorTempCode
  Stores information about a user’s temporary verification code for confirming their identity when logging in. This object is available in API version 37.0 and later.
  UiFormulaCriterion
  Represents a filter that helps define component visibility on a Lightning page. This object is available in API version 47.0 and later.
  UiFormulaRule
  Represents a set of one or more filters that define the conditions under which a component displays on a Lightning page. This object is available in API version 47.0 and later.
  UndecidedEventRelation
  Represents event participants (invitees or attendees) with the status Not Responded for a given event. This object is available in API versions 29.0 and later.
  UnifiedActivity
  Represents an activity that is automatically captured from Einstein Activity Capture (EAC) or other activity data, such as calls, manually logged tasks, and emails. This object consists of fields common to all types of activity-related objects such as Event, Task, EmailMessage, VoiceCall, VideoCall, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedActivityInsight
  Represents an insight related to a unified activity. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedActivityParticipant
  Represents a participant in an activity. For example, a participant in a voice call is someone who initiated the call or someone who received the call.This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedActivityRelation
  Represents a relationship between an activity and a related record that’s a target or topic of the activity. For example, a related record can be an opportunity, account, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedActvtyInsightKeyword
  Represents a keyword in a communication that triggered the activity insight. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedEmail
  Represents an email that was captured or synced from an EmailMessage or Task record. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedEmailParticipant
  Represents a participant in an email. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedMeeting
  Represents a meeting that was captured or synced from an Event record. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedMeetingParticipant
  Represents a participant in a meeting. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedTask
  Represents a business activity such as a to-do item. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedTaskParticipant
  Represents a participant in a task. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedVideoCall
  Represents a video call that is captured or synced from the VideoCall or Task record. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedVideoCallParticipant
  Represents a participant in a video call. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedVoiceCall
  Represents a voice call that is captured or synced from a VoiceCall or Task record. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnifiedVoiceCallParticipant
  Represents a participant in a voice call. This object is available for reports and dashboards in the Winter ’24 release and later.
  UnitOfMeasure
  Defines the units and systems of units used to express and account for quantities. This object is available in API version 61.0 and later.
  UriEventLog
  URI events contain details about user interaction with the web browser UI. This object is available in API version 55.0 and later.
  UsageImpactFactor
  Represents a collection of fields to set up the Usage Impact Factors used across jurisdictions and programs.This object is available in API version 58.0 and later.
  UsageImpactGroup
  Represents a collection of fields to set up the Usage Impact Groups used across jurisdictions and programs. This object is available in API version 58.0 and later.
  UsageImpactGroupFactor
  Represents a junction between an Usage Impact Group version and Usage Impact Factor. This object is available in API version 58.0 and later.
  UsageImpactGroupPgmMeasure
  Represents a junction between the program, product, and Usage Impact Group version. This object is available in API version 58.0 and later.
  UsageImpactGroupVersion
  Represents a collection of fields to set up the versions of Usage Impact Groups. This object is available in API version 58.0 and later.
  User
  Represents a user in your organization.
  UserAccessChange
  Represents a change related to user access. This object is available in API version 57.0 and later.
  UserAccessPolicy
  Represents a user access policy. This object is available in API version 57.0 and later.
  UserAccountTeamMember
  Represents a User on the default account team of another User.
  UserAppInfo
  Stores the last Lightning app logged in to. If the user hasn’t logged into Salesforce or if the user lost access to the last accessed app, the UserAppInfo object stores a Null value. This object is available in API version 38.0 and later.
  UserAppMenuCustomization
  Represents an individual user’s settings for items in the app menu or App Launcher. This object is available in API version 35.0 and later.
  UserAppMenuItem
  Represents the organization-wide settings for items in the app menu or App Launcher that the requesting user has access to in Setup. This object is available in API version 35.0 and later.
  UserAuthCertificate
  Represents a user authentication certificate in your org. A user certificate is a unique PEM-encoded X.509 digital certificate to authenticate individual users to your org. This object is available in API version 45.0 and later.
  UserConfigTransferButton
  Represents the association between a Chat configuration and a live chat button. This association allows users associated with a specific configuration to transfer chats to a button queue.
  UserConfigTransferSkill
  Represents the association between a Chat configuration and a skill. This association allows users associated with a specific configuration to transfer chats to agents who have that skill.
  UserCustomBadge
  Represents a custom badge for a user. This object is available in API version 38.0 and later.
  UserCustomBadgeLocalization
  Represents the translated version of a custom badge for a user. This object is available in API version 38.0 and later.
  UserDailyMetric
  Represents the daily engagement metrics for a user. This object is available in API version 52.0 and later.
  UserDailyMetricOwnerSharingRule
  Represents the rules for sharing the user daily metric with users other than the owner.
  UserDefinedLabel
  Represents a label created by a user to help organize, track, and find records. This object is available in API version 61.0 and later.
  UserDefinedLabelAssignment
  Represents a relationship between a record label and the item the user assigned it to. This object is available in API version 61.0 and later.
  UserDevice
  Represents information unique to a device. Available in API version 43.0 and later.
  UserDeviceApplication
  Represents information on applications installed on a device that is accessing Salesforce. Available in API version 43.0 and later.
  UserDeviceHistory
  Represents tracking information on the UserDevice sObject. This object is available in API version 50.0 and later.
  UserEmailCalendarSync
  Represents the user assignments of an Einstein Activity Capture configuration. This object is available in API version 49.0 and later.
  UserEmailPreferredPerson
  Represents a mapping for a user’s preferred record for an email address when multiple records match an email field.This object is available in API version 44.0 and later.
  UserEmailPreferredPersonShare
  Represents a sharing entry on a UserEmailPreferredPerson object. Sharing is not customizable for UserEmailPreferredPerson records.This object is available in API version 44.0 and later.
  UserLicense
  Represents a user license in your organization. A user license entitles a user to specific functionality and determines the profiles and permission sets available to the user.
  UserListView
  Represents the customizations a user made to a list view. This object is available in API version 32.0 and later.
  UserListViewCriterion
  Represents the criterion for a user’s customized list view. The criterion consists of the filters or sort order a user added to a list view for the Salesforce Mobile app. This object is available in API version 32.0 and later.
  UserLocationAssignment
  Represents the assignment between a location and a user. This object is available in API version 57.0 and later.
  UserLogin
  Represents the settings that affect a user’s ability to log into an organization. To access this object, you need the UserPermissions.ManageUsers permission. This object is available in API version 29.0 and later.
  UserMembershipSharingRule
  Represents the rules for sharing user records from a source group to a target group. A user record contains details about a user. Users who are members of the source group can be shared with members of the target group. The source and target groups can be based on roles, portal roles, public groups, or territories. This object is available in API version 26.0 and later.
  UserMonthlyMetric
  Represents the monthly engagement metrics for a user. This object is available in API version 52.0 and later.
  UserMonthlyMetricOwnerSharingRule
  Represents the rules for sharing the user monthly metric with users other than the owner.
  UserPackageLicense
  Represents a license for an installed managed package, assigned to a specific user. This object is available in API version 31.0 and later.
  UserPermissionAccess
  Represents the permissions accessibility for a current user. Available in API version 41.0 and later.
  UserPrioritizedRecord
  Represents records that Pipeline Inspection, Account Intelligence, Contact Intelligence, and Lead Intelligence users flag as important for tracking in pipeline and intelligence views and filters. This object is available in API version 53.0 and later.
  UserPreference
  Represents a functional preference for a specific user in your organization.
  UserProfile
  Represents a Chatter user profile.
  UserProvAccount
  Represents information that links a Salesforce user account with an account in a third-party (target) system, such as Google, for users of connected apps with Salesforce user provisioning enabled. This object is available in API version 33.0 and later.
  UserProvAccountStaging
  Temporarily stores user account information while a user completes the User Provisioning Wizard. This information that is stored in the UserProvAccount object when you click the button to collect and analyze accounts on the target system.
  UserProvMockTarget
  Represents an entity for testing user data before committing the data to a third-party system for user provisioning.
  UserProvisioningConfig
  Represents information for a flow to use during a user provisioning request process, such as the attributes for an update. This object is available in API version 34.0 and later.
  UserProvisioningLog
  Represents messages generated during the process of provisioning users for third-party applications. This object is available in API version 33.0 and later.
  UserProvisioningRequest
  Represents an individual provisioning request to create, update, or delete a single user account in a third-party service system (or another Salesforce organization). This object is available in API version 33.0 and later.
  UserRecordAccess
  Represents a user’s access to a set of records. This object is read only and is available in API version 24.0 and later. This object doesn’t consider whether a user’s access is blocked by a restriction rule.
  UserRole
  Represents a user role in your organization.
  UserServicePresence
  Represents a presence user’s real-time presence status. This object is available in API version 32.0 and later.
  UserSetupEntityAccess
  Represents the enabled custom permissions of the running user. This object is available in API version 48.0 and later.
  UserShare
  Represents a sharing entry on a user record. This object is available in API version 26.0 and later.
  UserSharedFeature
  For internal use only.
  UserTeamMember
  Represents a single User on the default opportunity team of another User.
  UserTerritory
  Represents a User who has been assigned to a Territory.
  UserTerritory2Association
  Represents an association (by assignment) between a territory and a user record. Available only if Sales Territories has been enabled.
  UserTerritory2AssocLog
  Represents a log of when a user is assigned and unassigned from a territory. This object is available in API version 57.0 and later.
  UserWorkList
  Represents a list of work items in the My Feed tab for Sales Engagement users.
  UserWorkListItem
  Represents an individual work item in the My Feed tab for Sales Engagement users.
  VendorCallCenterStatusMap
  Stores a mapping between a call center vendor agent status and a Salesforce presence status for an associated call center. This object is available in API version 54.0 and later.
  VerificationHistory
  Represents the past six months of your org users’ attempts to verify their identity. This object is available in API version 36.0 and later.
  VisualforceAccessMetrics
  Represents summary statistics for Visualforce pages.
  VisualforceRequestEventLog
  Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI). This object is available in API version 55.0 and later.
  VideoCall
  Represents a video call.
  VideoCallParticipant
  Represents a participant in a video call.
  VideoCallRecording
  Represents a recording from a video call, such as a video recording, a voice recording, or a transcript.
  VoiceCall
  Represents a call in Service Cloud Voice or Sales Dialer. For Service Cloud Voice, this can be a phone or Voice over Internet Protocol (VoIP) call. This object is available in API version 40.0 and later.
  VoiceCallMetrics
  Represents metrics for a VoiceCall lifecycle event, aggregated daily. This object is available in API version 56.0 and later.
  VoiceCallList
  Represents a prioritized list of numbers to call.
  VoiceCallListItem
  Represents a single phone number in a prioritized call list.
  VoiceCallQualityFeedback
  Represents feedback given by a Sales Dialer user about the quality of a VoiceCall .
  VoiceCallRecording
  Represents a call recording in Service Cloud Voice and Sales Dialer. Call recordings for Service Cloud Voice with Amazon Connect and for Service Cloud Voice with Partner Telephony from Amazon Connect are stored in S3 buckets on your Amazon Web Services (AWS) account and can be accessed via AWS. Call recordings for Sales Dialer are saved as files in Salesforce.
  VoiceCoaching
  Represents a call that is using call monitoring.
  VoiceLocalPresenceNumber
  Represents a phone number with the same area code as the person who’s being called.
  VoiceMailContent
  Represents a voicemail message left by a caller to the context user.
  VoiceMailGreeting
  Represents a custom greeting message that plays upon reaching a user’s voicemail. This object is available in API version 41.0 and later.
  VoiceMailMessage
  Represents a prerecorded voicemail message.
  VoiceUserLine
  Represents a user’s forwarding phone number.
  VoiceUserPreferences
  Represents the number the user displays when making outbound calls. This object is available in API version 41.0 and later.
  VoiceVendorInfo
  Represents information about the Service Cloud Voice or Sales Dialer provider’s vendor.
  VoiceVendorLine
  Represents a user’s phone number reserved with the vendor.
  Vote
  Represents a vote that a user has made on a Knowledge Article, Idea, or Reply.
  WarrantyTerm
  Represents warranty terms defining the labor, parts, and expenses covered, along with any exchange options, provided to rectify issues with products. This object is available in API version 50.0 and later.
  WaveAutoInstallRequest
  Provides access to the concrete object that represents a CRM Analytics auto-install request. The auto-install request tracks the progress of CRM Analytics applications created from CRM Analytics templates by the automated process user. This object is available in API version 38.0 and later.
  WebCart
  Represents an online shopping cart for a store built with B2B Commerce or D2C Commerce, with total amounts for products, shipping and handling, and taxes. This object is available in API version 49.0 and later.
  WebCartAdjustmentBasis
  Coupons that trigger promotions for the cart. When a customer tries to add a coupon to the cart, the store looks for promotions associated with the coupon. If a promotion results in a price adjustment, a WebCartAdjusmentBasis record is created. This object is available in API version 54.0 and later.
  WebCartAdjustmentGroup
  Group of price adjustments for a cart. This object is available in API version 52.0 and later.
  WebCartHistory
  WebCartHistory represents the history of changes to the values in the fields of the WebCart object.
  WebLink
  Represents a custom link to a URL or Scontrol.
  WebLinkLocalization
  Represents the translated value of the field label for a custom link to a URL or s-control when the Translation Workbench is enabled for your organization.
  WebStore
  Represents a B2B or D2C store. This object is available in API version 49.0 and later.
  WebstoreBuyerGroup
  Associates a webstore with a buyer group. Supports dynamically changing locales when buyers shop in orgs that are enabled for multiple languages and currencies. This object is available in API version 58.0 and later.
  WebStoreCatalog
  Represents the collection of products associated with a store. This object is available in API version 49.0 and later.
  WebStoreInventorySource
  Used to configure the inventory source for a webstore. This object is available in API version 57.0 and later.
  WebStoreMessageContent
  Represents the assocation of a managed content message record in CMS to a web store, along with other attributes that specify the application and intent of the message content. This object is available in API version 61.0 and later.
  WebStoreNetwork
  Represents the relationship between a web store and an experience site. This object is available in API version 49.0 and later.
  WebStorePricebook
  Represents a store price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.
  WebStoreSearchProdSettings
  Search settings for a WebStore product search. This object is available in API version 47.0 and later.
  Wishlist
  Represents a buyer-created list of WishlistItems in a store that’s built with B2B Commerce on Lightning. Available in API version 49.0 and later.
  WishlistItem
  Represents an item on a Wishlist in a store built with B2B Commerce for Lightning. Available in API version 49.0 and later.
  WorkAccess
  Used to grant or restrict user access to give badge definitions. Each badge definition record must have one WorkAccess record.
  WorkAccessShare
  Used to control Givers of WorkBadgeDefinition records.
  WorkBadge
  Represents information about who the badge was given to and which badge was given. A WorkBadge record is created for each recipient of a WorkBadgeDefinition.
  WorkBadgeDefinition
  Represents the attributes of a badge including the badge name, description, and image. Each WorkBadge record must have a lookup to a WorkBadgeDefinition since badge attributes (like badge name) are derived from the WorkBadgeDefinition object.
  WorkCapacityAvailability
  Represents the available work capacity for a specific time and service territory. This object is available in API version 59.0 and later.
  WorkCapacityLimit
  Represents the capacity limit in a specific service territory for a workstream or for the whole service territory in a given period. This object is available in API version 59.0 and later.
  WorkCapacityUsage
  Represents the capacity limit in a specific service territory for a workstream or for the whole service territory in a given period. This object is available in API version 59.0 and later.
  WorkCoaching
  Represents a single coaching relationship between two users. One of the users is defined as the coach and the other is defined as a coachee. WorkCoaching is feed-enabled so there is a private feed available to the coach and coachee.
  WorkDemographic
  Represents the field values used to specify slices in the workload forecasting and capacity planning. This object is available in API version 49.0 and later.
  WorkFeedback
  Represents the answer to a question that a person was asked via a feedback request. Also used to store offered feedback without linking it to a particular question.
  WorkFeedbackQuestion
  Represents a free-form text type or multiple choice question within a set of questions.
  WorkFeedbackQuestionSet
  Represents a set of questions being asked. The question set is used to link all the individual requests where different recipients were asked the same set of questions on the same subject.
  WorkFeedbackRequest
  Represents a single feedback request on a subject or topic (question) to a single recipient in the feedback application. In the case of offered feedback, WorkFeedbackRequest represents feedback that is offered about a subject. In the performance application, WorkFeedbackRequest represents a request for feedback on a set of questions from a question set, on a subject—for the recipient to complete and submit.
  WorkforceCapacity
  Represents the time series for actual or forecasted workforce allocation. This object is available in API version 51.0 and later.
  WorkforceCapacityUnit
  Represents the number of resources allocated or needed for a specific set of work items at a timestamp within a specific duration. This object is available in API version 51.0 and later.
  WorkGoal
  Represents the components of a goal, such as its description and associated metrics. This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals.
  WorkGoalCollaborator
  Represents collaborators on a WorkGoal object. This doesn’t include WorkGoal followers, which is handled by Chatter Feed Follow functionality. This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals.
  WorkGoalCollaboratorHistory
  Represents the history of changes to the values in the fields in a WorkGoalCollaborator object. Access is read-only.
  WorkGoalHistory
  Represents the history of changes to the values in the fields of a WorkGoal. Access is read-only. This object has been deprecated as of API version 35.0. Use the GoalHistory object to query historical information for WDC goals.
  WorkGoalLink
  Represents the relationship between two goals (many to many relationship). This object has been deprecated as of API version 35.0. Use the GoalLink object to query information about the relationship between two WDC goals.
  WorkGoalShare
  Represents a sharing entry on a WorkGoal object. This object has been deprecated as of API version 35.0. Use the GoalShare object to query information about sharing for WDC goals.
  Workload
  Represents the time series for work item volume and average handle time from aggregation and forecasting processes. This object is available in API version 49.0 and later.
  WorkloadUnit
  Represents the number of work items and average handle time in a specific time interval. This object is available in API version 49.0 and later.
  WorkOrder
  Represents field service work to be performed for a customer. This object is available in API version 36.0 and later.
  WorkOrderHistory
  Represents the history of changes made to tracked fields on a work order. This object is available in API version 36.0 and later.
  WorkOrderLineItem
  Represents a subtask on a work order in field service. This object is available in API version 36.0 and later.
  WorkOrderLineItemHistory
  Represents the history of changes made to tracked fields on a work order line item. This object is available in API version 36.0 and later.
  WorkOrderLineItemStatus
  Represents a possible status of a work order line item in field service.
  WorkOrderShare
  Represents a sharing entry on a work order. This object is available in API version 36.0 and later.
  WorkOrderStatus
  Represents a possible status of a work order in field service.
  WorkPerformanceCycle
  Represents feedback that is gathered to assess the performance of a specific set of employees.
  WorkPlan
  Represents a work plan for a work order or work order line item. This object is available in API version 52.0 and later.
  WorkPlanSelectionRule
  Represents a rule that selects a work plan for a work order or work order line item. This object is available in API version 52.0 and later.
  WorkPlanTemplate
  Represents a template for a work plan. This object is available in API version 52.0 and later.
  WorkPlanTemplateEntry
  Represents an object that associates a work step template with a work plan template. This object is available in API version 52.0 and later.
  WorkReward
  Used to store reward codes tied to a Reward Fund. Reward Funds must have at least one WorkReward record.
  WorkRewardFund
  Represents a Reward Fund and describes the Reward Fund attributes.
  WorkRewardFundType
  Represents the type of WorkRewardFund object.
  WorkStep
  Represents a work step in a work plan. This object is available in API version 52.0 and later.
  WorkStepStatus
  Represents a picklist for a status category on a work step. This object is available in API version 52.0 and later.
  WorkStepTemplate
  Represents a template for a work step. This object is available in API version 52.0 and later.
  WorkThanks
  Represents the source and message of a thanks post.
  WorkType
  Represents a type of work to be performed in Field Service and Lightning Scheduler. Work types are templates that can be applied to work order or work order line items. This object is available in API version 38.0 and later.
  WorkTypeGroup
  Represents a grouping of work types used to categorize types of appointments available in Lightning Scheduler, or to define scheduling limits in Field Service. This object is available in API version 45.0 and later.
  WorkTypeGroupMember
  Represents the relationship between a work type and the work type group it belongs to. This object is available in API version 45.0 and later.

