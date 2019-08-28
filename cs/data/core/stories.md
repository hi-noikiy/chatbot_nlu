## only greeting
* greeting
    - slot_reset
    - utter_greet

## only chatty
* chatty
    - slot_reset
    - utter_chatty

## only byebye
* byebye
    - slot_reset
    - utter_goodbye
    
## direct ask question with clarified product info 小闪
* question
    - utter_ask_product_info
* clarify_product{"product": "小闪"}
    - slot{"product": "小闪"}
    - query_action
* intent_deny
    - utter_out_of_scope

## direct ask question with clarified product info T1mini
* question
    - utter_ask_product_info
* clarify_product{"product": "T1mini"}
    - slot{"product": "T1mini"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info T1
* question
    - utter_ask_product_info
* clarify_product{"product": "T1"}
    - slot{"product": "T1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info T1
* question
    - utter_ask_product_info
* clarify_product{"product": "T1"}
    - slot{"product": "T1"}
    - query_action
* intent_choose
    - return_chosen
    - slot_reset
    
## direct ask question with clarified product info T2
* question
    - utter_ask_product_info
* clarify_product{"product": "T2"}
    - slot{"product": "T2"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info V2 Pro
* question
    - utter_ask_product_info
* clarify_product{"product": "V2pro"}
    - slot{"product": "V2pro"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info P1
* question
    - utter_ask_product_info
* clarify_product{"product": "P1"}
    - slot{"product": "P1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info M1
* question
    - utter_ask_product_info
* clarify_product{"product": "M1"}
    - slot{"product": "M1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with clarified product info K1
* question
    - utter_ask_product_info
* clarify_product{"product": "K1"}
    - slot{"product": "K1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info D2
* question
    - utter_ask_product_info
* clarify_product{"product": "D2"}
    - slot{"product": "D2"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info D1S
* question
    - utter_ask_product_info
* clarify_product{"product": "D1S"}
    - slot{"product": "D1S"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with clarified product info V1s
* question
    - utter_ask_product_info
* clarify_product{"product": "V1s"}
    - slot{"product": "V1s"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask question with product 小闪
* question{"product": "小闪"}
    - slot{"product": "小闪"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset
    
## direct ask with product T1 mini
* question{"product": "T1mini"}
    - slot{"product": "T1mini"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product T1
* question{"product": "T1"}
    - slot{"product": "T1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product T2
* question{"product": "T2"}
    - slot{"product": "T2"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product V2 pro
* question{"product": "V2pro"}
    - slot{"product": "V2pro"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product P1
* question{"product": "P1"}
    - slot{"product": "P1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product M1
* question{"product": "M1"}
    - slot{"product": "M1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product K1
* question{"product": "K1"}
    - slot{"product": "K1"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product D2
* question{"product": "D2"}
    - slot{"product": "D2"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product D1S
* question{"product": "D1S"}
    - slot{"product": "D1S"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset

## direct ask question with product V1s
* question{"product": "V1s"}
    - slot{"product": "V1s"}
    - query_action
* intent_deny
    - utter_out_of_scope
    - slot_reset