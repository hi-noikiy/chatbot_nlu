## only greeting
* greeting
    - utter_greet

## only chatty
* chatty
    - utter_chatty

## question without product info
* greeting
    - utter_greet
* question
    - utter_goodbye

## question with product 小闪
* greeting
    - utter_greet
* question{"product": "小闪"}
    - utter_greet

## question with product T1 mini
* greeting
    - utter_greet
* question{"product": "T1mini"}
    - utter_greet

## question with product T1
* greeting
    - utter_greet
* question{"product": "T1"}
    - slot{"product": "T1"}
    - utter_greet

## question with product T2
* greeting
    - utter_greet
* question{"product": "T2"}
    - utter_greet

## question with product V2 pro
* greeting
    - utter_greet
* question{"product": "V2pro"}
    - utter_greet

## question with product P1
* greeting
    - utter_greet
* question{"product": "P1"}
    - utter_greet

## question with product M1
* greeting
    - utter_greet
* question{"product": "M1"}
    - utter_greet

## question with product K1
* greeting
    - utter_greet
* question{"product": "K1"}
    - utter_greet

## question with product D2
* greeting
    - utter_greet
* question{"product": "D2"}
    - utter_greet

## question with product D1S
* greeting
    - utter_greet
* question{"product": "D1S"}
    - utter_greet

## question with product V1s
* greeting
    - utter_greet
* question{"product": "V1s"}
    - utter_greet