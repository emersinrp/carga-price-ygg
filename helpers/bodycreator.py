from random import choice

class BodyCreator:
    @staticmethod
    def create():
        LIST_CNPJS = [
            "51033629000179",
            "39309210000100",
            "23626669000199",
            "39309210000100",
            "96189790000174"
        ]
        PAYMENT_CONDITION = [
            "R019",
            "R007",
            "0319",
            "R012",
            "0719",
            "R005"
        ]
        CONDITION = [
            "Y100",
            "YB2B"
        ]
        FIFO_RANGE_CODE = [
            "Z100",
            "Z098",
            "Z101"
        ]
        SKU_CODES = [
            "000000000000539325",
            "000000000000732112",
            "000000000000597975",
            "000000000000220647",
            "000000000000344002",

        ]

        query = "query QueryCargaTest($fiscal_code_buyer: String,\
                $document_id_buyer: String,\
                $buyer_code: String,\
                $distribution_channel_code: String!,\
                $payment_condition: String!,\
                $condition: String!,\
                $units_of_measurements: [UnitsOfMeasurements!],\
                $currencies: [Currencies!],\
                $sales_document_type: String!,\
                $item_category_code: [String!],\
                $fifo_range: [String!],\
                $sku_code: [String!])\
                {get_price(filters:{fifo_range: $fifo_range,\
                payment_code: $payment_condition\
                condition: $condition\
                distribution_channel_code: $distribution_channel_code, \
                item_category_code: $item_category_code,\
                sales_document_type: $sales_document_type,\
                rounded: 6,\
                fiscal_code_buyer: $fiscal_code_buyer,\
                document_id_buyer: $document_id_buyer,\
                buyer_code: $buyer_code,\
                units_of_measurements: $units_of_measurements,\
                currencies: $currencies,\
                sku_code: $sku_code,\
                pagination_filter: {first: \"50\"}})"

        agregators = " {agregators {sales_region_agregator \
                {sales_region sales_organization_agregator \
                {sales_organization price_sales_agregator \
                {edges {cursor node {distribution_channel_code activity_sector payment_condition material_type_size_agregator\
                {kilograms {brl {currency_name price_itens {sku_code item_category_agregator \
                {item_category_code price_detail \
                {base_price discount_percent max_price discount_price max_price_percentage min_price min_price_percentage \
                payment_percentage price tributary_substitution_discount_price tributary_substitution_price taxes \
                {icms {country tax_percentage tax_value} \
                tributary_substitution {country tax_percentage tax_value}}}}}}}}}}}}}}\
                page_info {end_cursor has_next_page has_previous_page start_cursor}}}"

        variables = {
            "fiscal_code_buyer": choice(LIST_CNPJS),
            "document_id_buyer": "",
            "distribution_channel_code": "10",
            "payment_condition": choice(PAYMENT_CONDITION),
            "condition": choice(CONDITION),
            "currencies": "brazilian_real",
            "sales_document_type": "YB2B",
            "fifo_range": choice(FIFO_RANGE_CODE),
            "sku_code": choice(SKU_CODES)
        }

        body = {
            "query": query+agregators,
            "variables": variables,
            "operationName": "QueryCargaTest"

        }
        return body
