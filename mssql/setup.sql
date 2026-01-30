-- Reset và setup lại toàn bộ 3 database với đầy đủ thí sinh (1-1000)
-- ==========================================================

-- 1. Setup THISINH_BAC
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'THISINH_BAC') CREATE DATABASE THISINH_BAC;
GO
USE THISINH_BAC;
GO
IF OBJECT_ID('ThiSinh', 'U') IS NOT NULL DROP TABLE ThiSinh;
CREATE TABLE ThiSinh (
    SBD INT PRIMARY KEY,
    HoTen NVARCHAR(100),
    KhuVuc NVARCHAR(10),
    DiemToan FLOAT, DiemVan FLOAT, DiemAnh FLOAT, 
    DiemLy FLOAT, DiemHoa FLOAT, DiemSinh FLOAT
);
GO
DECLARE @i INT = 1;
WHILE @i <= 300
BEGIN
    INSERT INTO ThiSinh VALUES (
        @i, 
        CONCAT(
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Nguyễn', N'Trần', N'Lê', N'Phạm', N'Hoàng', N'Phan', N'Vũ', N'Đặng', N'Bùi', N'Đỗ'), ' ', 
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Văn', N'Thị', N'Minh', N'Thanh', N'Đức', N'Ngọc', N'Quang', N'Hữu', N'Anh', N'Kim'), ' ', 
            CHOOSE(CAST(RAND()*10+1 AS INT), N'An', N'Bình', N'Cường', N'Dũng', N'Giang', N'Hương', N'Khánh', N'Linh', N'Nam', N'Sơn')
        ),
        N'Miền Bắc', ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2)
    );
    SET @i = @i + 1;
END
GO

-- 2. Setup THISINH_TRUNG
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'THISINH_TRUNG') CREATE DATABASE THISINH_TRUNG;
GO
USE THISINH_TRUNG;
GO
IF OBJECT_ID('ThiSinh', 'U') IS NOT NULL DROP TABLE ThiSinh;
CREATE TABLE ThiSinh (
    SBD INT PRIMARY KEY,
    HoTen NVARCHAR(100),
    KhuVuc NVARCHAR(10),
    DiemToan FLOAT, DiemVan FLOAT, DiemAnh FLOAT, 
    DiemLy FLOAT, DiemHoa FLOAT, DiemSinh FLOAT
);
GO
DECLARE @k INT = 301;
WHILE @k <= 600
BEGIN
    INSERT INTO ThiSinh VALUES (
        @k, 
        CONCAT(
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Phan', N'Võ', N'Trương', N'Bùi', N'Ngô', N'Hồ', N'Dương', N'Đặng', N'Lý', N'Mai'), ' ', 
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Hữu', N'Thanh', N'Ngọc', N'Quang', N'Anh', N'Minh', N'Tuyết', N'Xuân', N'Tuấn', N'Phương'), ' ', 
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Thành', N'Hùng', N'Kiên', N'Long', N'Quân', N'Triết', N'Việt', N'Yến', N'Hà', N'Tuệ')
        ),
        N'Miền Trung', ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2)
    );
    SET @k = @k + 1;
END
GO

-- 3. Setup THISINH_NAM
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'THISINH_NAM') CREATE DATABASE THISINH_NAM;
GO
USE THISINH_NAM;
GO
IF OBJECT_ID('ThiSinh', 'U') IS NOT NULL DROP TABLE ThiSinh;
CREATE TABLE ThiSinh (
    SBD INT PRIMARY KEY,
    HoTen NVARCHAR(100),
    KhuVuc NVARCHAR(10),
    DiemToan FLOAT, DiemVan FLOAT, DiemAnh FLOAT, 
    DiemLy FLOAT, DiemHoa FLOAT, DiemSinh FLOAT
);
GO
DECLARE @j INT = 601;
WHILE @j <= 1000
BEGIN
    INSERT INTO ThiSinh VALUES (
        @j, 
        CONCAT(
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Lý', N'Huỳnh', N'Lâm', N'Dương', N'Mai', N'Vương', N'Trịnh', N'Đoàn', N'Tô', N'Cao'), ' ', 
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Thành', N'Kim', N'Minh', N'Quốc', N'Trọng', N'Khải', N'Duy', N'Thảo', N'Trang', N'Oanh'), ' ', 
            CHOOSE(CAST(RAND()*10+1 AS INT), N'Phát', N'Đạt', N'Thịnh', N'Vượng', N'Khang', N'Phúc', N'Lộc', N'Thọ', N'Tâm', N'Hào')
        ),
        N'Miền Nam', ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2), ROUND(RAND()*6+4,2)
    );
    SET @j = @j + 1;
END
GO
