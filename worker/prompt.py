
keys_extraction="""From the above document, read the values of the following fields:
-ccn (Claim Number)
-patientMember (Patient Name)
-authorizedAmount (Amunt for which claim is setteled)
-date (Date of letter)
-mdIdNo (Unique Health Identification Number)
-policyNumber (Policy Number)
-admissionDate (Date of admission)
-dischargeDate (Date of discharge)
-tdsAmount (TDS Amount)
-finalPayableAmount (Final Paymentable Amount)
-lodgedAmount (Amount which is requested)

no need to return any extra text just return them as a JSON key value pair format for ex: {"ccn":"the value we got"}
Also remove any extra unrelevent character."""
