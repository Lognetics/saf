/* Synia Aid Foundation — site configuration.
   This is the only file that needs editing to connect the site's live services.
   Leave a value as an empty string and the site degrades gracefully:
     - forms fall back to a pre-filled email to info@syniafoundation.org
     - the donate button directs the donor to the bank-transfer panel
     - no analytics script is loaded at all

   formEndpoint   POST target for contact, partnership, volunteer, ambassador
                  and newsletter forms. Must store the submission, route it to
                  the correct inbox and send the sender an acknowledgement.
   donateEndpoint Checkout URL for the payment gateway (Paystack or Flutterwave;
                  Stripe does not operate for Nigerian entities).
   analyticsSrc   Script URL for privacy-respecting analytics. Loaded ONLY after
                  the visitor accepts optional cookies. Never hard-code an
                  analytics tag into the page head.
*/
window.SAF_CONFIG = {
  formEndpoint:   '',
  donateEndpoint: '',
  analyticsSrc:   ''
};
