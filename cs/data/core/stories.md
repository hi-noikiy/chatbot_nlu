## only greeting
* greeting
    - utter_greet

## only chatty
* chatty
    - utter_chatty

## only byebye
* byebye
    - utter_goodbye
    
## direct ask question without product info
* question
    - utter_ask_product_info
* clarify_product
    - utter_confirm_product
    
## direct ask question with product 小闪
* question{"product": "小闪"}
    - utter_greet
    
## direct ask with product T1 mini
* question{"product": "T1mini"}
    - slot{"product": "T1mini"}
    - utter_greet

## direct ask question with product T1
* question{"product": "T1"}
    - slot{"product": "T1"}
    - utter_greet

## direct ask question with product T2
* question{"product": "T2"}
    - slot{"product": "T2"}
    - utter_greet

## direct ask question with product V2 pro
* question{"product": "V2pro"}
    - slot{"product": "V2pro"}
    - utter_greet

## direct ask question with product P1
* question{"product": "P1"}
    - slot{"product": "P1"}
    - utter_greet

## direct ask question with product M1
* question{"product": "M1"}
    - slot{"product": "M1"}
    - utter_greet

## direct ask question with product K1
* question{"product": "K1"}
    - slot{"product": "K1"}
    - utter_greet

## direct ask question with product D2
* question{"product": "D2"}
    - slot{"product": "D2"}
    - utter_greet

## direct ask question with product D1S
* question{"product": "D1S"}
    - slot{"product": "D1S"}
    - utter_greet

## direct ask question with product V1s
* question{"product": "V1s"}
    - slot{"product": "V1s"}
    - utter_greet

## question without product info and confirmed T1mini
* greeting
    - utter_greet
* question
    - utter_ask_product_info
* clarify_product{"product": "T1mini"}
    - utter_confirm_product
* byebye
    - utter_goodbye

## question with product 小闪
* greeting
    - utter_greet
* question{"product": "小闪"}
    - slot{"product": "小闪"}
    - utter_greet

## question with product T1 mini
* greeting
    - utter_greet
* question{"product": "T1mini"}
    - slot{"product": "T1mini"}
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
    - slot{"product": "T2"}
    - utter_greet

## question with product V2 pro
* greeting
    - utter_greet
* question{"product": "V2pro"}
    - slot{"product": "V2pro"}
    - utter_greet

## question with product P1
* greeting
    - utter_greet
* question{"product": "P1"}
    - slot{"product": "P1"}
    - utter_greet

## question with product M1
* greeting
    - utter_greet
* question{"product": "M1"}
    - slot{"product": "M1"}
    - utter_greet

## question with product K1
* greeting
    - utter_greet
* question{"product": "K1"}
    - slot{"product": "K1"}
    - utter_greet

## question with product D2
* greeting
    - utter_greet
* question{"product": "D2"}
    - slot{"product": "D2"}
    - utter_greet

## question with product D1S
* greeting
    - utter_greet
* question{"product": "D1S"}
    - slot{"product": "D1S"}
    - utter_greet

## question with product V1s
* greeting
    - utter_greet
* question{"product": "V1s"}
    - slot{"product": "V1s"}
    - utter_greet