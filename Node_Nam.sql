CREATE DATABASE THISINH_NAM
USE THISINH_NAM

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

DECLARE @i INT = 501;
WHILE @i <= 1000
BEGIN
    INSERT INTO ThiSinh (SBD, HoTen, KhuVuc, DiemToan, DiemVan, DiemAnh, DiemLy, DiemHoa, DiemSinh)
    VALUES (
        @i, 
        CONCAT('Hoc Sinh Nam ', @i), 
        'Mien Nam',
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2),
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2), 
        ROUND(RAND() * 10, 2)
    );
    SET @i = @i + 1;
END;

SELECT * FROM ThiSinh
Where SBD = 783