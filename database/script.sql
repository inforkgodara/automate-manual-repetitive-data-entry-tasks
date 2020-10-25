/* Create table */
CREATE TABLE sales_orders
(
  id             NUMBER(10) PRIMARY KEY,
  order_id       VARCHAR2(15 BYTE)              NOT NULL,
  order_date     DATE                           NOT NULL,
  ship_date      DATE,
  ship_mode      VARCHAR2(20 BYTE),
  customer_id    VARCHAR2(20 BYTE),
  customer_name  VARCHAR2(80 BYTE),
  segement       VARCHAR2(20 BYTE),
  city           VARCHAR2(40 BYTE),
  state          VARCHAR2(40 BYTE),
  region         VARCHAR2(40 BYTE),
  product_id     VARCHAR2(20 BYTE),
  category       VARCHAR2(20 BYTE),
  sub_category   VARCHAR2(25 BYTE),
  product_name   VARCHAR2(260 BYTE),
  sales          NUMBER(12,2),
  quantity       NUMBER(10,2),
  discount       NUMBER(12,2),
  profit         NUMBER(12,2)
)

/* Create sequence */
CREATE SEQUENCE sales_orders_sequence
  START WITH 0
  MAXVALUE 9999999999
  MINVALUE 1
  NOCYCLE
  CACHE 20
  NOORDER;

/* Create trigger */
CREATE OR REPLACE TRIGGER sales_orders_on_insert
  BEFORE INSERT ON sales_orders   FOR EACH ROW
BEGIN
  SELECT sales_orders_sequence.nextval
  INTO :new.id
  FROM dual;
END;
/