resource "azurerm_network_interface" "main" {
  name                = "unique-nic-diallo"
  location            = "francecentral"
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal_diallo"
    subnet_id                     = data.azurerm_subnet.existing.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.main.id
  }
}

resource "azurerm_public_ip" "main" {
  name                = "unique-publicip-diallo"
  location            = "francecentral"
  resource_group_name = var.resource_group_name
  allocation_method   = "Dynamic"
}
