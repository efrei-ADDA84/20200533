variable "subscription_id" {
  description = "ID de l'abonnement Azure"
  type        = string
  default     = "765266c6-9a23-4638-af32-dd1e32613047"
}

variable "resource_group_name" {
  description = "Nom du groupe de ressources"
  type        = string
  default     = "ADDA84-CTP"
}

variable "virtual_network_name" {
  description = "Nom du réseau virtuel existant"
  type        = string
  default     = "network-tp4"
}

variable "subnet_name" {
  description = "Nom du sous-réseau existant"
  type        = string
  default     = "internal"
}
