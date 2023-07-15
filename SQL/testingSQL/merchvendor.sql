USE indieheads;

-- DROP TABLE IF EXISTS MERCHVENDOR;

CREATE TABLE MERCHVENDOR (
    MerchVendor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Merch_ID INT,
    Vendor_ID INT,
    QuantitySupplied INT,
    FOREIGN KEY (Merch_ID) REFERENCES MERCH(Merch_ID),
    FOREIGN KEY (Vendor_ID) REFERENCES VENDOR(Vendor_ID)
);

INSERT INTO MERCHVENDOR (Merch_ID, Vendor_ID, QuantitySupplied)
VALUES
(1, 4, 500),
(2, 4, 600),
(5, 4, 550),
(3, 5, 400),
(4, 5, 700);
