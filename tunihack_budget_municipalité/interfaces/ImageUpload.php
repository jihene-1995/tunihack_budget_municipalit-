<?php
// Check if the form was submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){
    // Check if file was uploaded without errors
    if(isset($_FILES["photo"]) && $_FILES["photo"]["error"] == 0){
        $allowed = array("jpg" => "image/jpg", "jpeg" => "image/jpeg", "gif" => "image/gif", "png" => "image/png");
        $filename = $_FILES["photo"]["name"];
        $filetype = $_FILES["photo"]["type"];
        $filesize = $_FILES["photo"]["size"];
    
        // Verify file extension
        $ext = pathinfo($filename, PATHINFO_EXTENSION);
      
    
        // Verify file size - 5MB maximum
       
    
        // Verify MYME type of the file
       
            if(file_exists("images/" . $filename)){
                echo $filename . " is already exists.";
            } else{
                move_uploaded_file($_FILES["photo"]["tmp_name"], "images/" . $filename);

header( 'Location: http://localhost/mag/index.html' ) ;

                echo "Your file was uploaded successfully.";
            } 
        }
    } else{
        echo "Error: " . $_FILES["photo"]["error"];
    }

?>