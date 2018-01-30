## 0.3 - Improved stable client
* Added Consumption.by_aggregates()
* Consumption.by_cups() now passes CUPS as HTTP params
* Isolated packages for each functionality
  * client.consumptions.by_cups() replaces client.consumptions_by_cups()
  * client.consumptions.by_aggregates() replaces client.consumptions_by_aggregates()
* Consumptions arguments are now passed as body data instead of GET params
* Fixed BUG at API init (asserting URL) #16
* Fixed BUG at install process race condition

## 0.2.0 - First productive client!
* Package renamed to "orakwlum_client"
* Drone testing for py2.7 and py3.6

## 0.1.0 - First Release
* okW API interface
* okW Client
