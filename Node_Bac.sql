CREATE DATABASE THISINH_BAC
USE THISINH_BAC

CREATE TABLE ThiSinh (
    SBD INT PRIMARY KEY,
    HoTen NVARCHAR(100),
    KhuVuc NVARCHAR(10),

    DiemToan FLOAT,
    DiemVan FLOAT,
    DiemAnh FLOAT,

    DiemLy FLOAT,
    DiemHoa FLOAT,
    DiemSinh FLOAT
);

DECLARE @i INT = 1;
WHILE @i <= 500
BEGIN
    INSERT INTO ThiSinh (SBD, HoTen, KhuVuc, DiemToan, DiemVan, DiemAnh, DiemLy, DiemHoa, DiemSinh)
    VALUES (
        @i, 
        CONCAT('Hoc Sinh Bac ', @i), 
        'Mien Bac',
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2),
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2)
    );
    SET @i = @i + 1;
END;


