## Sample Curl Request for LocalHost (Pin to Top)

curl -X POST http://localhost:8000/claim-question \
-H "Content-Type: application/json" \
-d '{
  "question": "Why was this claim denied?\n\n{\"patient_name\":\"Jane Doe\",\"patient_date_of_birth\":\"1985-01-15\",\"patient_id\":\"123456789\",\"provider_name\":\"Dr. John Smith, MD\",\"provider_npi\":\"1234567890\",\"date_of_service\":\"2024-08-15\",\"cpt_code\":\"30410\",\"diagnosis_code\":\"Z41.1\",\"charge_amount\":7500.00,\"insurance_plan_name\":\"XYZ Health Plan\",\"claim_status\":\"Pending Denial\",\"reason_for_procedure\":\"Patient requested rhinoplasty for aesthetic improvement, no medical necessity.\"}"
}'

## Sample Curl Request for Deployment (Pin below LocalHost)

curl -X POST https://claimquestion.replit.app/claim-question \
-H "Content-Type: application/json" \
-d '{
  "question": "Why was this claim denied?\n\n{\"patient_name\":\"Jane Doe\",\"patient_date_of_birth\":\"1985-01-15\",\"patient_id\":\"123456789\",\"provider_name\":\"Dr. John Smith, MD\",\"provider_npi\":\"1234567890\",\"date_of_service\":\"2024-08-15\",\"cpt_code\":\"30410\",\"diagnosis_code\":\"Z41.1\",\"charge_amount\":7500.00,\"insurance_plan_name\":\"XYZ Health Plan\",\"claim_status\":\"Pending Denial\",\"reason_for_procedure\":\"Patient requested rhinoplasty for aesthetic improvement, no medical necessity.\"}"
}'

## Documentation for Claim-Question API Endpoint
### Endpoint: `/claim-question`
This endpoint processes claim questions and returns a random claim amount.
#### Request
- Method: POST
- Content-Type: application/json
- Body:
  ```json
  {
    "question": "string"
  }
The question field can contain any string, but the content is not used to determine the response.

Response
Content-Type: application/json
Body:
{
  "answer": "string"
}
The answer field will contain a string in the format: "Your claim costs X dollars", where X is a random even number between 2 and 100.

Sample curl request
curl -X POST http://localhost:8000/claim-question \
  -H "Content-Type: application/json" \
  -d '{"question": "How many dollars is this claim?"}'
Sample response
{
  "answer": "Your claim costs 64 dollars"
}