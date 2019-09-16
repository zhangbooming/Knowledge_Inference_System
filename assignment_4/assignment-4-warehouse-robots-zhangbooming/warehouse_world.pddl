(define (domain warehouse)
	(:requirements :typing)
	(:types robot pallette - bigobject
        	location shipment order saleitem)
  	(:predicates
    	(ships ?s - shipment ?o - order)
    	(orders ?o - order ?si - saleitem)
    	(unstarted ?s - shipment)
    	(started ?s - shipment)
    	(complete ?s - shipment)
    	(includes ?s - shipment ?si - saleitem)

    	(free ?r - robot)
    	(has ?r - robot ?p - pallette)

    	(packing-location ?l - location)
    	(packing-at ?s - shipment ?l - location)
    	(available ?l - location)
    	(connected ?l - location ?l - location)
    	(at ?bo - bigobject ?l - location)
    	(no-robot ?l - location)
    	(no-pallette ?l - location)

    	(contains ?p - pallette ?si - saleitem)
  )

   (:action startShipment
      :parameters (?s - shipment ?o - order ?l - location)
      :precondition (and (unstarted ?s) (not (complete ?s)) (ships ?s ?o) (available ?l) (packing-location ?l))
      :effect (and (started ?s) (packing-at ?s ?l) (not (unstarted ?s)) (not (available ?l)))
   )

   (:action robotMove
      :parameters(?r - robot ?l_1 - location ?l_2 - location)
      :precondition(and (at ?r ?l_1) (no-robot ?l_2) (connected ?l_1 ?l_2))
      :effect(and (not (at ?r ?l_1)) (not (no-robot ?l_2)) (no-robot ?l_1) (at ?r ?l_2))
   )

   (:action robotMoveWithPallette
      :parameters(?r - robot ?l_1 - location ?l_2 - location ?p - pallette)
      :precondition(and (at ?r ?l_1) (at ?p ?l_1) (no-robot ?l_2) (no-pallette ?l_2) (connected ?l_1 ?l_2))
      :effect(and (not (at ?r ?l_1)) (not (at ?p ?l_1)) (not (no-robot ?l_2)) (not (no-pallette ?l_2)) (no-robot ?l_1) (no-pallette ?l_1) (at ?r ?l_2) (at ?p ?l_2))
   )

   (:action moveItemFromPalletteToShipment
      :parameters(?s - shipment ?o - order ?l - location ?p - pallette ?si - saleitem)
      :precondition(and (ships ?s ?o) (orders ?o ?si) (started ?s) (not (complete ?s)) (packing-location ?l) (packing-at ?s ?l) (not (available ?l)) (at ?p ?l) (contains ?p ?si))
      :effect(and (includes ?s ?si) (not (contains ?p ?si)))
   )

   (:action completeShipment
      :parameters(?s - shipment ?o - order ?l - location)
      :precondition(and (ships ?s ?o) (started ?s) (not (complete ?s)) (packing-location ?l) (packing-at ?s ?l) (not (available ?l)))
      :effect(and (complete ?s) (available ?l))
   )

)

