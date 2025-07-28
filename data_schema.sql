CREATE TABLE covid_stats (
    id INT IDENTITY(1,1) PRIMARY KEY,
    report_date DATE NOT NULL,
    country VARCHAR(100),
    cases INT,
    todayCases INT,
    deaths INT,
    todayDeaths INT,
    recovered INT,
    active INT,
    mortality_rate FLOAT,
    recovery_rate FLOAT
);
