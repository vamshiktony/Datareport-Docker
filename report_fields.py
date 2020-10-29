IRN_DOC_REPORT_FIELDS = "''::text AS unique_document, ''::text AS nic_code, irp_response_message, irn_status, ackno, ackdt, pwc_response_status, pwc_response_validation_remarks, pwc_response_validation_status, pwc_response_message,"\
                        "load_id, user_gstin, ''::text AS version, irn, sourcesystem, is_irn, is_ewb, email, trandtls_taxsch, trandtls_outwardinward, trandtls_subtype, "\
                        "trandtls_subtypedescription, trandtls_suptyp, trandtls_regrev, trandtls_typ, trandtls_ecmgstin,trandtls_igstonintra, trandtls_diffpercentage, trandtls_taxability, trandtls_interintra, "\
                        "trandtls_cnclflg, cancel_reason, cancel_remark, docdtls_typ, docdtls_no, docdtls_dt, docdtls_reasonforcndn, sellerdtls_gstin, sellerdtls_lglnm, sellerdtls_trdnm, "\
                        "sellerdtls_addr1, sellerdtls_addr2, sellerdtls_loc, sellerdtls_pin, sellerdtls_stcd, sellerdtls_ph, sellerdtls_em, sellerdtls_suppliercode, buyerdtls_gstin, "\
                        "buyerdtls_lglnm, buyerdtls_trdnm, buyerdtls_addr1, buyerdtls_addr2, buyerdtls_loc, buyerdtls_pin, buyerdtls_stcd, buyerdtls_pos, buyerdtls_ph, buyerdtls_em, "\
                        "buyerdtls_customercode, dispdtls_gstin, dispdtls_nm, dispdtls_addr1, dispdtls_addr2, dispdtls_loc, dispdtls_pin, dispdtls_stcd_name, shipdtls_gstin, shipdtls_lglnm,"\
                        "shipdtls_trdnm, shipdtls_addr1, shipdtls_addr2, shipdtls_loc, shipdtls_pin, shipdtls_stcd_name, il_slno, il_ordlineref, il_prdslno, il_itemcode, il_prdnm, "\
                        "il_prddesc, il_hsncd, il_isservc, il_barcde, il_qty, il_freeqty, il_unit, il_unitprice, il_totamt, il_discount, il_othchrg, il_vat, il_centralexcise, il_stateexcise,"\
                        "expdtls_expduty, il_valuebeforebcd, il_bcd, il_pretaxval, il_assamt, il_gstrt, il_cgstrt, il_sgstrt, il_igstrt, il_cesrt, il_cessnonadvolrt, il_statecesrt, il_igstamt,"\
                        "il_cgstamt, il_sgstamt, il_cesamt, il_cesnonadvlamt, il_statecesamt, il_statecesnonadvlamt, il_totitemval, il_orgcntry, il_bchdtls_nm, il_bchdtls_expdt, il_bchdtls_wrdt,"\
                        "il_attribdtls, il_eligibilityitc, il_itcigst, il_itccgst, il_itcsgst, il_itccess, il_natureofexpense, il_glcdrvnexpns, il_glcdigst, il_glcdcgst, il_glcdsgst, il_glcdcess,"\
                        "il_glcdigstitc, il_glcdcgstitc, il_glcdsgstitc, il_glcdcessitc, il_mis1, il_mis2, il_mis3, il_mis4, il_mis5, il_mis6, il_mis7, il_mis8, il_mis9, il_mis10, il_mis11,"\
                        "il_mis12, il_mis13, il_mis14, il_mis15, il_mis16, il_mis17, il_mis18, il_mis19, il_mis20, il_mis21, il_mis22, il_mis23, il_mis24, il_mis25, il_mis26, il_mis27, il_mis28,"\
                        "il_mis29, il_mis30, il_fu1, il_fu2, il_fu3, il_fu4, il_fu5, il_fu6, il_fu7, il_fu8, il_fu9, il_fu10, valdtls_assval, valdtls_cgstval, valdtls_sgstval, valdtls_igstval, "\
                        "valdtls_cesval, valdtls_stcesval, valdtls_cesnonadval, valdtls_disc, valdtls_othchrg, valdtls_rndoffamt, valdtls_totinvval, valdtls_totinvvalfc, paydtls_nm, paydtls_mode,"\
                        "paydtls_fininsbr, paydtls_payterm, paydtls_payinstr, paydtls_crtrn, paydtls_dirdr, paydtls_crday, paydtls_paidamt, paydtls_paymtdue, paydtls_accdet, refdtls_invrm,"\
                        "refdtls_docperddtls_invstdt, refdtls_docperddtls_invenddt, refdtls_precdocdtls, refdtls_contrdtls, refdtls_accountingdocno, refdtls_accountingdocdt, refdtls_sono, refdtls_sodt, refdtls_advncrfno,"\
                        "refdtls_advncrfdt, refdtls_advncamt, addldocdtls, expdtls_refclm, expdtls_shipbno, expdtls_shipbdt, expdtls_port, expdtls_forcur, expdtls_cntcode, ewbdtls_transid, "\
                        "ewbdtls_distance, ewbdtls_transname, ewbdtls_transmode_name, ewbdtls_transdocno, ewbdtls_transdocdt, ewbdtls_vehno, ewbdtls_vehtype, whthdrsdtls_tan, whthdrsdtls_vndrstid, "\
                        "whthdrsdtls_whttrnsctgry, whthdrsdtls_srcedctyp, whthdrsdtls_lndscrptn, whthdrsdtls_dtofddctn, whthdrsdtls_entdt, whthdrsdtls_projctcd, whthdrsdtls_txcderp, whthdrsdtls_crrncy,"\
                        "whthdrsdtls_exchngrt, whthdrsdtls_exchngtyp, whthdrsdtls_ntfctn_21_2012, whthdrsdtls_cntrremittance, whthdrsdtls_isgrssdup, il_whtitem_podscrptn, il_whtitem_vchrid, "\
                        "il_whtitem_dbtcrdtidntfr, il_whtitem_grssexpnsamt, il_whtitem_tdsbsamt, il_whtitem_tdssctn, il_whtitem_tdsrt, il_whtitem_tdsamt, il_whtitem_offstglcd, il_whtitem_tdsglcd,"\
                        "bu, sbu, location, user_name, companycode, companyname, trackingno, transactioncount,  returnperiod, tdsapplcbl, mis ->> 'Mis31'::text AS mis31, "\
                        "mis ->> 'Mis32'::text AS mis32, mis ->> 'Mis33'::text AS mis33, mis ->> 'Mis34'::text AS mis34, mis ->> 'Mis35'::text AS mis35, mis ->> 'Mis36'::text AS mis36,"\
                        "mis ->> 'Mis37'::text AS mis37, mis ->> 'Mis38'::text AS mis38, mis ->> 'Mis39'::text AS mis39, mis ->> 'Mis40'::text AS mis40, mis ->> 'Mis41'::text AS mis41, mis ->> 'Mis42'::text AS mis42,"\
                        "mis ->> 'Mis43'::text AS mis43, mis ->> 'Mis44'::text AS mis44, mis ->> 'Mis45'::text AS mis45, mis ->> 'Mis46'::text AS mis46, mis ->> 'Mis47'::text AS mis47, mis ->> 'Mis48'::text AS mis48,"\
                        "mis ->> 'Mis49'::text AS mis49, mis ->> 'Mis50'::text AS mis50, mis ->> 'Mis51'::text AS mis51, mis ->> 'Mis52'::text AS mis52, mis ->> 'Mis53'::text AS mis53, mis ->> 'Mis54'::text AS mis54,"\
                        "mis ->> 'Mis55'::text AS mis55, mis ->> 'Mis56'::text AS mis56, mis ->> 'Mis57'::text AS mis57, mis ->> 'Mis58'::text AS mis58, mis ->> 'Mis59'::text AS mis59, mis ->> 'Mis60'::text AS mis60,"\
                        "fu ->> 'Fu11'::text AS fu11, fu ->> 'Fu12'::text AS fu12, fu ->> 'Fu13'::text AS fu13, fu ->> 'Fu14'::text AS fu14, fu ->> 'Fu15'::text AS fu15, fu ->> 'Fu16'::text AS fu16,"\
                        "fu ->> 'Fu17'::text AS fu17, fu ->> 'Fu18'::text AS fu18, fu ->> 'Fu19'::text AS fu19, fu ->> 'Fu20'::text AS fu20, fu ->> 'Fu21'::text AS fu21, fu ->> 'Fu22'::text AS fu22,"\
                        "fu ->> 'Fu23'::text AS fu23, fu ->> 'Fu24'::text AS fu24, fu ->> 'Fu25'::text AS fu25, fu ->> 'Fu26'::text AS fu26, fu ->> 'Fu27'::text AS fu27, fu ->> 'Fu28'::text AS fu28,"\
                        "fu ->> 'Fu29'::text AS fu29, fu ->> 'Fu30'::text AS fu30, initiated_date, created_date, created_by, initiated_by, updated_by,"\
                        "updated_date, is_exclude, exclude_reason, exclude_remark, update_history, udid, "\
                        "ewb_details ->> 'EwbDt'::text AS ewbdt, "\
                        "ewb_details ->> 'EwbNo'::text AS ewbno, "\
                        "ewb_details ->> 'EwbValidTill'::text AS ewbvalidtill,"\
                        "ewb_details ->> 'EwbGenerationStatus'::text AS ewbstatus, "\
                        "is_active, comments,"\
                        "''::text AS itemcnt, "\
                        "''::text AS mainhsncode, "\
                        "nic_qr_image, cancel_date, signedqrcode,"\
                        "nic_response_plaintext_json -> 'SignedQRCode' -> 'data' as itemcnt_mainhsn, nic_error_details"
IRN_DOC_REPORT_HEADERS = [ "Unique_Documents", "NIC_Code", "Irp_Response_Message","Irn_Status","AckNo","AckDt","PwC Validation Code","Pwc_Response_Validation_Remarks","Pwc_Response_Validation_Status", "Pwc_Response_Message",
                            "Load ID", "User GSTIN", "Version", "IRN", "Source_System", "Is_IRN", "Is_Ewb", "E-mail_ID", "TranDtls_TaxSch", "Outward_Inward", "Sub_type",
                            "Sub_type_description", "TranDtls_SupTyp", "TranDtls_Regrev", "TranDtls_Typ", "TranDtls_EcmGstin","Trandtls_Igstonintra", "Diff_percentage", "Taxability", "Inter_Intra",
                            "Cancelled_Flag", "Cancelled_Reason", "Cancelled_Remarks", "DocDtls_Typ", "DocDtls_No", "DocDtls_Dt", "Reason_for_CN_DN",
                            "SellerDtls_Gstin", "SellerDtls_LglNm", "SellerDtls_TrdNm", "SellerDtls_Addr1", "SellerDtls_Addr2", "SellerDtls_Loc", "SellerDtls_Pin", "Sellerdtls_Stcd",
                            "SellerDtls_Ph", "SellerDtls_Em", "Supplier_Code", "BuyerDtls_Gstin", "BuyerDtls_LglNm", "BuyerDtls_TrdNm", "BuyerDtls_Addr1", "BuyerDtls_Addr2", "BuyerDtls_Loc",
                            "BuyerDtls_Pin", "Buyerdtls_Stcd", "BuyerDtls_Pos", "BuyerDtls_Ph", "BuyerDtls_Em", "Customer_Code", "DispDtls_Gstin", "DispDtls_Nm", "DispDtls_Addr1",
                            "DispDtls_Addr2", "DispDtls_Loc", "DispDtls_Pin", "DispDtls_Stcd", "ShipDtls_Gstin", "ShipDtls_LglNm", "ShipDtls_TrdNm", "ShipDtls_Addr1", "ShipDtls_Addr2",
                            "ShipDtls_Loc", "ShipDtls_Pin", "ShipDtls_Stcd", "ItemsList_SlNo", "ItemsList_OrdLineRef", "ItemsList_PrdSlNo", "Item_code", "ItemsList_PrdNm", "ItemsList_PrdDesc",
                            "ItemsList_HsnCd", "ItemsList_IsServc", "ItemsList_BarCde", "ItemsList_Qty", "ItemsList_FreeQty", "ItemsList_Unit", "ItemsList_UnitPrice", "ItemsList_TotAmt",
                            "ItemsList_Discount", "ItemsList_OthChrg", "VAT", "Central_Excise", "State_Excise", "ExpDtls_ExpDuty", "Value_before_BCD", "BCD", "ItemsList_PreTaxVal", "ItemsList_AssAmt",
                            "ItemsList_GstRt", "ItemsList_CgstRt", "ItemsList_SgstRt", "ItemsList_IgstRt", "ItemsList_CesRt", "ItemsList_Cess_Non_Advol_Rt", "ItemsList_StateCesRt",
                            "ItemsList_IgstAmt", "ItemsList_CgstAmt", "ItemsList_SgstAmt", "ItemsList_CesAmt", "ItemsList_CesNonAdvlAmt", "ItemsList_StateCesAmt", "ItemsList_StateCesNonAdvlAmt",
                            "ItemsList_TotItemVal", "ItemsList_OrgCntry", "ItemsList_Batch_Nm", "ItemsList_Batch_ExpDt", "ItemsList_Batch_WrDt", "ItemsList_AttribDtls",
                            "Eligibility_ITC", "ITC_IGST", "ITC_CGST", "ITC_SGST", "ITC_Cess", "Nature_of_expense", "GL_code_Revenue_expense", "GL_code_IGST",
                            "GL_code_CGST", "GL_code_SGST", "GL_code_Cess", "GL_code_IGST_ITC", "GL_code_CGST_ITC", "GL_code_SGST_ITC", "GL_code_Cess_ITC", "MIS_1",
                            "MIS_2", "MIS_3", "MIS_4", "MIS_5", "MIS_6", "MIS_7", "MIS_8", "MIS_9", "MIS_10","MIS_11", "MIS_12", "MIS_13", "MIS_14", "MIS_15", "MIS_16", "MIS_17", "MIS_18", "MIS_19", "MIS_20", "MIS_21", "MIS_22", "MIS_23", "MIS_24", "MIS_25", "MIS_26", "MIS_27",
                            "MIS_28", "MIS_29", "MIS_30", "FU_1", "FU_2", "FU_3", "FU_4", "FU_5", "FU_6", "FU_7", "FU_8", "FU_9", "FU_10", "ValDtls_AssVal", "ValDtls_CgstVal", "ValDtls_SgstVal",
                            "ValDtls_IgstVal", "ValDtls_CesVal", "ValDtls_StCesVal", "ValDtls_CesNonAdval", "ValDtls_Discount", "ValDtls_OthChrg", "ValDtls_RndOffAmt", "ValDtls_TotInvVal",
                            "ValDtls_TotInvValFc", "PayDtls_Nm", "PayDtls_Mode", "PayDtls_FinInsBr", "PayDtls_PayTerm", "PayDtls_PayInstr", "PayDtls_CrTrn", "PayDtls_DirDr", "PayDtls_CrDay",
                            "PayDtls_PaidAmt", "PayDtls_PaymtDue", "PayDtls_AcctDet", "RefDtls_InvRm", "RefDtls_DocPerdDtls_InvStDt", "RefDtls_DocPerdDtls_InvEndDt", "RefDtls_PrecDocDtls", "RefDtls_ContrDtls",
                            "Accounting_doc_No", "Accounting_doc_dt", "SO_No", "SO_dt", "Advance_Ref_No", "Advance_Ref_dt", "Advance_Amt", "AddlDocDtls", "ExpDtls_RefClm", "ExpDtls_ShipBNo",
                            "ExpDtls_ShipBDt", "ExpDtls_Port",  "ExpDtls_ForCur", "ExpDtls_CntCode", "EwbDtls_TransId", "EwbDtls_Distance", "EwbDtls_TransName", "EwbDtls_TransMode", "EwbDtls_TransDocNo",
                            "EwbDtls_TransDocDt", "EwbDtls_VehNo", "EwbDtls_VehType", "TAN", "Vendor_site_ID", "WHT_Trans_Category", "Source_Doc_Type", "Line_description",
                            "Date_of_deduction", "Entry_date", "Project_code", "Tax_code_ERP", "Currency", "Exchange_rate", "Exchange_type", "Notification_21_2012", "Country_remittance",
                            "Is_grossed_up", "PO_description", "Voucher_ID", "Debit_Credit_identifier", "Gross_expense_amt", "TDS_base_amt", "TDS_section", "TDS_Rate", "TDS_Amt", "Offset_GL_Code",
                            "TDS_GL_Code", "BU", "SBU", "Location", "User", "Company_Code", "Company_Name", "Tracking_No", "Transaction_count", "Return_Period", "TDS_applicable",
                            "MIS_31", "MIS_32", "MIS_33", "MIS_34", "MIS_35", "MIS_36", "MIS_37", "MIS_38", "MIS_39", "MIS_40", "MIS_41", "MIS_42", "MIS_43", "MIS_44", "MIS_45", "MIS_46",
                            "MIS_47", "MIS_48", "MIS_49", "MIS_50", "MIS_51", "MIS_52", "MIS_53", "MIS_54", "MIS_55", "MIS_56", "MIS_57", "MIS_58","MIS_59", "MIS_60", "FU_11", "FU_12", "FU_13",
                            "FU_14", "FU_15", "FU_16", "FU_17", "FU_18", "FU_19", "FU_20", "FU_21", "FU_22", "FU_23", "FU_24", "FU_25", "FU_26", "FU_27", "FU_28", "FU_29", "FU_30" ,
                            "Inititated_Date", "Created_Date","Created_By", "Initiated_By","Updated_By","Updated_Date", "Is_Exclude", "Exclude_Reason", "Exclude/Include Remark",
                            "Update History", "UDID", "EWB Date", "EWB No", "EWB Valid Upto", "EWB Status", "Active", "Comments", "ItemCnt", "MainHsnCode", "QR Code Base 64", 
                            "CancelDate", "SignedQrCode"]