<script>
  $(document).ready(function() {
    var orderId = 0; // Initialize the order ID
    
    $("#start-order-btn").click(function() {
      // Get the current date and time
      var currentDate = new Date();
      var currentTime = currentDate.toLocaleTimeString();
      
      // Get the logged-in user name (replace 'getLoggedInUserName()' with your actual code to retrieve the user name)
      var userName = getLoggedInUserName();
      
      // Increment the order ID
      orderId++;
      
      // Display the details
      $("#order-details").html(
        "<p>Order ID: " + orderId + "</p>" +
        "<p>Date: " + currentDate.toDateString() + "</p>" +
        "<p>Time: " + currentTime + "</p>" +
        "<p>User Name: " + userName + "</p>"
      );
      
      // Enable the add to order buttons
      $(".add-to-order-btn").prop("disabled", false);
    });
    
    // Rest of the code...
    
  });
</script>
