USE lead_gen_business;
-- 1. Total revenue for March 2012
SELECT SUM(amount) AS total_revenue
FROM billing
WHERE charged_datetime >= '2012/03/01' AND charged_datetime < '2012/04/01';

-- 2. Total revenue from client with id 2
SELECT SUM(amount) AS total_revenue
FROM billing
WHERE client_id = 2;

-- 3. All sites owned by client with id 10
SELECT domain_name
FROM sites
WHERE client_id = 10;

-- 4. Total monthly sites created per year for client 1 and client 20
SELECT YEAR(created_datetime) AS year, MONTH(created_datetime) AS month, COUNT(*) AS total_sites
FROM sites
WHERE client_id = 1
GROUP BY year, month;

SELECT YEAR(created_datetime) AS year, MONTH(created_datetime) AS month, COUNT(*) AS total_sites
FROM sites
WHERE client_id = 20
GROUP BY year, month;

-- 5. Total leads per site between Jan 1 and Feb 15 2011
SELECT site_id, COUNT(*) AS total_leads
FROM leads
WHERE registered_datetime >= '2011/01/01' AND registered_datetime <= '2011/02/15'
GROUP BY site_id;

-- 6. Client names and total leads between Jan 1 and Dec 31 2011
SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011/01/01' AND leads.registered_datetime <= '2011/12/31'
GROUP BY clients.client_id;

-- 7. Client names and total leads per month (months 1-6 of 2011)
SELECT clients.first_name, clients.last_name, MONTH(leads.registered_datetime) AS month, COUNT(*) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE YEAR(leads.registered_datetime) = 2011 AND MONTH(leads.registered_datetime) BETWEEN 1 AND 6
GROUP BY clients.client_id, month;

-- 8a. Client names and leads per site between Jan 1 and Dec 31 2011 ordered by client ID
SELECT clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011/01/01' AND leads.registered_datetime <= '2011/12/31'
GROUP BY clients.client_id, sites.site_id
ORDER BY clients.client_id;

-- 8b. All clients, site names, and total leads for all time
SELECT clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.site_id;

-- 9a. Total revenue per client per month (integer month)
SELECT client_id, YEAR(charged_datetime) AS year, MONTH(charged_datetime) AS month, SUM(amount) AS total_revenue
FROM billing
GROUP BY client_id, year, month
ORDER BY client_id;

-- 9b. Total revenue per client per month (month name)
SELECT client_id, YEAR(charged_datetime) AS year, MONTHNAME(charged_datetime) AS month, SUM(amount) AS total_revenue
FROM billing
GROUP BY client_id, year, month
ORDER BY client_id;

-- 10. All sites per client in single field
SELECT clients.first_name, clients.last_name, GROUP_CONCAT(sites.domain_name SEPARATOR ', ') AS sites
FROM clients
JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;
