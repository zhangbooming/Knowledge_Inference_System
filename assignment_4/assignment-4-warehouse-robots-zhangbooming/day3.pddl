(define (problem day3)
  (:domain warehouse)
  (:objects
    shipment1 shipment2 - shipment
    order1 order2 - order
    loc1 loc2 loc3 pack1 - location
    robot1 robot2 - robot
    pallette1 pallette2 - pallette
    socks1 socks2 book1 - saleitem
    )

  (:init
    (ships shipment1 order1)
    (orders order1 socks1)
    (orders order1 book1)
    (unstarted shipment1)
    (ships shipment2 order2)
    (orders order2 socks2)
    (unstarted shipment2)
    (packing-location pack1)
    (available pack1)
    (contains pallette1 socks1)
    (contains pallette1 socks2)
    (contains pallette2 book1)
    (free robot1)
    (free robot2)
    (connected loc1 loc2)
    (connected loc2 loc1)
    (connected loc2 loc3)
    (connected loc3 loc2)
    (connected loc2 pack1)
    (connected pack1 loc2)
    (at pallette1 loc1)
    (at pallette2 loc2)
    (at robot1 loc1)
    (at robot2 loc2)
    (no-robot loc3)
    (no-robot pack1)
    (no-pallette loc3)
    (no-pallette pack1)
    (available pack1)
    )
  (:goal (and (includes shipment1 socks1)
              (includes shipment1 book1)
              (includes shipment2 socks2)))
)
