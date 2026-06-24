<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout (Version 1.0.4 FINAL RUN)</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,400;0,700;1,400&family=Impact&display=swap');

        body {
            background-color: #F0FDF4; /* Weak sickly green background that clashes with purple/yellow */
            font-family: 'Comic Neue', cursive;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .checkout-container {
            background: #FFFFFF;
            border: 5px double #000000;
            border-radius: 0px; /* Sharp uncomfortable edges */
            width: 100%;
            max-width: 550px;
            padding: 30px;
            box-shadow: 10px 10px 0px #000000; /* Harsh heavy shadow */
        }

        /* Fake Placeholder Logo to stand in for your file */
        .fake-logo {
            font-family: 'Impact', sans-serif;
            font-size: 32px;
            color: #9333EA; /* Theme Purple */
            text-align: center;
            letter-spacing: 4px;
            margin-bottom: 15px;
            text-transform: uppercase;
        }

        /* Terribly aggressive warning banner */
        .bad-banner {
            background-color: #FFDE59; /* Neon Yellow */
            border: 3px dashed #FF3131; /* Bright Red */
            padding: 15px;
            text-align: left;
            margin-bottom: 25px;
        }

        .bad-banner h2 {
            color: #0000FF; /* Pure saturated Blue */
            font-size: 18px;
            margin: 0 0 8px 0;
            font-weight: bold;
            text-align: center;
        }

        .bad-banner p {
            color: #FF3131;
            font-size: 13px;
            margin: 4px 0;
            font-weight: bold;
            line-height: 1.4;
        }

        h3 {
            color: #000000;
            border-bottom: 2px solid #000000;
            padding-bottom: 5px;
            margin-top: 20px;
            font-size: 18px;
        }

        .cart-row {
            display: flex;
            justify-content: space-between;
            font-size: 15px;
            margin-bottom: 15px;
        }

        /* Intentionally messy, unaligned layout form elements */
        .form-group {
            margin-bottom: 12px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
            font-size: 13px;
            margin-bottom: 4px;
            color: #1E293B;
        }

        .form-group input, .form-group select {
            width: 95%;
            padding: 8px;
            border: 2px solid #334155;
            font-family: 'Comic Neue', cursive;
            background-color: #FFFBEB; /* Off-color input backgrounds */
        }

        /* Confusing 3-column split for expiry data with labels inside placeholder text */
        .triple-row {
            display: flex;
            gap: 5px;
            width: 99%;
        }

        .triple-row input {
            width: 83%;
        }

        /* Tiny sneaky text layout hidden at the bottom */
        .sneaky-checkboxes {
            margin-top: 20px;
            background: #F8FAFC;
            padding: 10px;
            border: 1px solid #CBD5E1;
        }

        .sneaky-checkboxes label {
            display: flex;
            align-items: flex-start;
            font-size: 9px; /* Microscopic font size */
            color: #64748B;
            margin-bottom: 8px;
            cursor: pointer;
        }

        .sneaky-checkboxes input {
            margin-right: 8px;
            margin-top: 1px;
        }

        /* Completely broken button hierarchy */
        .button-container {
            display: flex;
            gap: 15px;
            margin-top: 25px;
        }

        .btn {
            flex: 1;
            padding: 12px;
            font-family: 'Comic Neue', cursive;
            font-weight: bold;
            font-size: 14px;
            cursor: pointer;
            border: none;
            text-transform: uppercase;
        }

        /* Cancel is big, beautiful, and draws all attention */
        .btn-cancel {
            background-color: #0000FF;
            color: white;
            box-shadow: 0px 4px 10px rgba(0, 0, 255, 0.3);
        }

        /* actual purchase button is tiny, muted, lowercase, and looks broken/disabled */
        .btn-submit {
            background-color: #E2E8F0;
            color: #94A3B8;
            border: 1px solid #CBD5E1;
            font-size: 11px;
        }
    </style>
</head>
<body>

<div class="checkout-container">
    
    <div class="fake-logo">Shark Tank</div>

    <div class="bad-banner">
        <h2>⚠️ SYSTEM LOCKED BY SYSTEM ADMINISTRATOR</h2>
        <p><strong>SECURITY CIPHER:</strong> <span style="font-family: monospace; font-size: 15px; background: white; padding: 2px 6px; border: 1px solid black; color: black;">Wkh sdvvzrug lv Srzhu</span></p>
        <p><strong>HINT 1:</strong> The shift key algorithm used to lock this screen is '3'.</p>
        <p><strong>HINT 2:</strong> The third character of the decrypted text string resolves to the letter 'e'.</p>
    </div>

    <h3>Your Items</h3>
    <div class="cart-row">
        <span>Premium Ultra-Soft Gaming Socks (Size: Random)</span>
        <strong>$89.99</strong>
    </div>

    <h3>Delivery & Financial Data Entry</h3>
    
    <div class="form-group">
        <label>Enter Country First</label>
        <input type="text" value="Worldwide">
    </div>

    <div class="form-group">
        <label>Type everything here (First Name, Middle, Last Name, Title, Apartment Number)</label>
        <input type="text" placeholder="Johnathan Doe Esq Apt 4B...">
    </div>

    <div class="form-group">
        <label>Select Payment Method Type</label>
        <select>
            <option>- Select One -</option>
            <option>Crypto Token</option>
            <option>Gift Voucher Code</option>
            <option>Standard Credit Card</option>
            <option>Bank Wire transfer</option>
        </select>
    </div>

    <div class="form-group">
        <label>Type your 16 digit card number out loud (No spaces allowed)</label>
        <input type="text" placeholder="4111222233334444">
    </div>

    <div class="form-group">
        <label>Expirations & Back Codes</label>
        <div class="triple-row">
            <input type="text" placeholder="Month (MM)">
            <input type="text" placeholder="Year (YYYY)">
            <input type="text" placeholder="Secret Code">
        </div>
    </div>

    <div class="sneaky-checkboxes">
        <label>
            <input type="checkbox" checked>
            Sign me up for the weekly magazine and share my physical home address with trusted third-party marketing affiliates.
        </label>
        <label>
            <input type="checkbox" checked>
            Automatically renew this ordering attempt as a monthly recurring subscription fee of $89.99 without notifying my email.
        </label>
    </div>

    <div class="button-container">
        <button class="btn btn-cancel">CANCEL ORDER AND ERASE ALL HISTORY</button>
        <button class="btn btn-submit">submit data</button>
    </div>

</div>

</body>
</html>
