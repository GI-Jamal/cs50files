-- Keep a log of any SQL queries you execute as you solve the mystery.

-- The following queries are to determine the number of records in each table
SELECT COUNT(*) FROM airports;
SELECT COUNT(*) FROM crime_scene_reports;
SELECT COUNT(*) FROM people;
SELECT COUNT(*) FROM atm_transactions;
SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM phone_calls;
SELECT COUNT(*) FROM bakery_security_logs;
SELECT COUNT(*) FROM interviews;
SELECT COUNT(*) FROM bank_accounts;
SELECT COUNT(*) FROM passengers;

-- The following query is to inspect the crime scene report from the theft
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28;

-- The following query is to inspect the transcript of interviews taken on the day of the theft
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

-- The following query is to inspect the Leggett Street ATM transaction logs from the day of the theft
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street';

-- The following query is to inspect the call logs of duration less than or equal to one minute on the day of the theft
SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration <= 60;

-- The following query is to inspect the bakery security logs from the day and time of the theft
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25 ORDER BY hour ASC, minute ASC;

-- The following query is to inspect all flights out of fiftyville on the day after the theft
SELECT * FROM airports WHERE full_name LIKE 'Fiftyville%';
SELECT * FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC;

-- The following query is to inspect the passenger records for the flight to New York City out of Fiftyville the day after the theft
SELECT * FROM passengers WHERE flight_id = 36;

-- The following query amalgamates the above information to determine the potential theft suspect
SELECT DISTINCT(PE.name), ATM.account_number, PA.passport_number, PE.phone_number, PE.id, PE.license_plate, PE.passport_number
FROM people AS PE
JOIN passengers AS PA
ON PE.passport_number = PA.passport_number
JOIN bakery_security_logs AS BA
ON PE.license_plate = BA.license_plate
JOIN phone_calls AS PH
ON PE.phone_number = PH.caller
JOIN bank_accounts AS BAC
ON PE.id = BAC.person_id
JOIN atm_transactions AS ATM
ON BAC.account_number = ATM.account_number
WHERE PA.flight_id = 36
AND ATM.account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street')
AND BA.license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25)
AND PH.caller IN (SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration <= 60);

-- Potential theft suspect
+-------+----------------+-----------------+----------------+--------+---------------+-----------------+
| name  | account_number | passport_number |  phone_number  |   id   | license_plate | passport_number |
+-------+----------------+-----------------+----------------+--------+---------------+-----------------+
| Bruce | 49610011       | 5773159633      | (367) 555-5533 | 686048 | 94KL13X       | 5773159633      |
+-------+----------------+-----------------+----------------+--------+---------------+-----------------+

-- Tracing Bruce's phone records lead to the potential theft accomplie
SELECT * FROM people WHERE phone_number = '(375) 555-8161';
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 |                 | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+