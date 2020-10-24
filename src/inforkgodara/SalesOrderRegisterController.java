package inforkgodara;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Window;

public class SalesOrderRegisterController {
    @FXML
    private TextField orderId;

    @FXML
    private TextField orderDate;

    @FXML
    private TextField shipDate;
    
    @FXML
    private TextField shipMode;
    
    @FXML
    private TextField customerID;
    
    @FXML
    private TextField customerName;
    
    @FXML
    private TextField segment;
    
    @FXML
    private TextField region;
    
    @FXML
    private TextField city;
    
    @FXML
    private TextField state;
    
    @FXML
    private TextField productID;
    
    @FXML
    private TextField productName;
    
    @FXML
    private TextField category;
    
    @FXML
    private TextField subCategory;
    
    @FXML
    private TextField sales;
    
    @FXML
    private TextField quantity;
    
    @FXML
    private TextField discount;
    
    @FXML
    private TextField profit;

    @FXML
    private Button submitButton;

    @FXML
    protected void handleSubmitButtonAction(ActionEvent event) {
        Window owner = submitButton.getScene().getWindow();

        AlertHelper.showAlert(Alert.AlertType.CONFIRMATION, owner, "Information", 
                "Order no " + orderId.getText() + " saved successfully.");
    }
}