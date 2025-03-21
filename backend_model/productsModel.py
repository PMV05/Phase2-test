# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array
productList = [['1', "Airpods 4", 'Apple', 'desc here', 'Yes', 'Earphone', 'White', 'imagenes_audifonos/apple/apple_airpods_4.jpg', '15', 'active', '129.00', '129.00'],
               ['2', 'Airpods Max', 'Apple', 'desc', 'Yes', 'Headphone', 'White', 'imagenes_audifonos/apple/apple_airpods_max.jpg', '3', 'active', '549.00', '549.00'],
               ['3', 'Airpods Pro 2', 'Apple', 'desc', 'Yes', 'Earphone', 'White', 'imagenes_audifonos/apple/apple_airpods_pro2.jpg', '3', 'active', '249.00', '249.00'],
               ['4', 'Flex', 'Beats', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/beats/beats_flex.jpg', '3', 'active', '69.99', '69.99'],
               ['5', 'Solo 4', 'Beats', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/beats/beats_solo_4.jpg', '3', 'active', '199.99', '199.99'],
               ['6', 'Solo Buds', 'Beats', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/beats/beats_solo_buds.jpg', '3', 'active', '79.99', '79.99'],
               ['7', 'Studio Pro', 'Beats', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/beats/beats_studio_pro.jpg', '3', 'active', '349.99', '349.99'],
               ['8', 'Quiet Comfort Ultra Earbuds', 'Bose', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/bose/bose_quietcomfort_ultra_earbuds.jpg', '3', 'active', '299.00', '299.00'],
               ['9', 'Quiet Comfort Ultra', 'Bose', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/bose/bose_quietcomfort_ultra.jpg', '3', 'active', '429.00', '429.00'],
               ['10', 'Quiet Comfort', 'Bose', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/bose/bose_quietcomfort.jpg', '3', 'active', '349.00', '349.00'],
               ['11', 'Ultra Open Earbuds', 'Bose', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/bose/bose_ultra_open_earbuds.jpg', '3', 'active', '299.00', '299.00'],
               ['12', "HS80 RGB", 'Corsair', 'desc here', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/corsair/corsair_hs80_rgb.jpg', '15', 'active', '149.99', '149.99'],
               ['13', 'HS55 Surround v2', 'Corsair', 'desc', 'Yes', 'Headset', 'White', 'imagenes_audifonos/corsair/corsair_hs55_surround.jpg', '3', 'active', '59.99', '59.99'],
               ['14', 'Virtuoso Max', 'Corsair', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/corsair/corsair_virtuoso_max.jpg', '3', 'active', '329.99', '329.99'],
               ['15', 'Void RGB Elite', 'Corsair', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/corsair/corsair_void_rgb_elite.jpg', '3', 'active', '109.99', '109.99'],
               ['16', 'Cloud Alpha', 'HyperX', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/hyper_x/hyperx_cloud_alpha.jpg', '3', 'active', '199.99', '199.99'],
               ['17', 'Cloud Stinger Core', 'HyperX', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/hyper_x/hyperx_cloud_stinger_core.jpg', '3', 'active', '79.99', '79.99'],
               ['18', 'Cloud Stinger 2', 'HyperX', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/hyper_x/hyperx_cloud_stinger.jpg', '3', 'active', '49.99', '49.99'],
               ['19', 'Cloud III', 'HyperX', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/hyper_x/hyperx_cloud3.jpg', '3', 'active', '99.99', '99.99'],\
               ['20', 'Astro A50 X', 'Logitech G', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/logitech_g/logitech_atro_a50.jpg', '3', 'active', '379.99', '379.99'],
               ['21', 'G432', 'Logitech G', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/logitech_g/logitech_g432_wired.jpg', '3', 'active', '79.99', '79.99'],
               ['22', 'G733 Lightspeed', 'Logitech G', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/logitech_g/logitech_g733_lightspeed.jpg', '3', 'active', '149.99', '149.99'],
               ['23', 'Pro Wireless', 'Logitech G', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/logitech_g/logitech_pro_x_wireless.jpg', '3', 'active', '159.99', '159.99'],
               ['24', 'Barracuda x Chroma', 'Razer', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/razer/razer_barracuda_chroma.jpg', '3', 'active', '129.99', '129.99'],
               ['25', 'BlackShark V2 Pro', 'Razer', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/razer/razer_blackshark_v2_pro.jpg', '3', 'active', '199.99', '199.99'],
               ['26', 'Hammerhead Pro Hyperspeed', 'Razer', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/razer/razer_hammerhead_hyperspeed.jpg', '3', 'active', '196.96', '196.96'],
               ['27', 'Kraken V4 Pro', 'Razer', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/razer/razer_kraken_v4_pro.jpg', '3', 'active', '399.99', '399.99'],
               ['28', 'Crusher ANC 2', 'Skullcandy', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/skullcandy/skullcandy_crusher_anc_2.jpg', '3', 'active', '229.00', '229.00'],
               ['29', 'Dime EVO', 'Skullcandy', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/skullcandy/skullcandy_dime_evo.jpg', '3', 'active', '49.99', '49.99'],
               ['30', 'Icon ANC', 'Skullcandy', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/skullcandy/skullcandy_icon_anc_.jpg', '3', 'active', '99.99', '99.99'],
               ['31', 'Set', 'Skullcandy', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/skullcandy/skullcandy_set.jpg', '3', 'active', '31.99', '31.99'],
               ['32', 'ULT Wear', 'Sony', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/sony/sony_ult_wear.jpg', '3', 'active', '199.99', '199.99'],
               ['33', 'WF-1000XM5', 'Sony', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/sony/sony_wf_xm5.jpg', '3', 'active', '299.99', '299.99'],
               ['34', 'WH-1000XM5', 'Sony', 'desc', 'Yes', 'Headphone', 'Black', 'imagenes_audifonos/sony/sony_wh_xm5.jpg', '3', 'active', '399.99', '399.99'],
               ['35', 'WI-C100', 'Sony', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/sony/sony_wi_c100.jpg', '3', 'active', '34.99', '34.99'],
               ['36', 'Arctis Nova Pro', 'SteelSeries', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/steelseries/steelseries_arctis_nova_pro.jpg', '3', 'active', '349.99', '349.99'],
               ['37', 'Arctis Gamebuds', 'SteelSeries', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/steelseries/steelseries_arctis_gamebuds.jpg', '3', 'active', '159.99', '159.99'],
               ['38', 'Arctis Pro Wireless', 'SteelSeries', 'desc', 'Yes', 'Headset', 'Black', 'imagenes_audifonos/steelseries/steelseries_arctis_pro_wireless.jpg', '3', 'active', '349.99', '349.99'],
               ['39', 'TUSQ', 'SteelSeries', 'desc', 'Yes', 'Earphone', 'Black', 'imagenes_audifonos/steelseries/steelseries_tusq.jpg', '3', 'active', '39.99', '39.99']]


def getProductsModel():
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in productList:
        if product[0] == prodID:
            return product
