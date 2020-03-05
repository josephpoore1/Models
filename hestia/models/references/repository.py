from hestia.models.references.json_data_mappings import DATA_MAPPING
from hestia.data_client.data_client import DataClient
import pandas as pd


class ReferencesRepository(DataClient):
    def __init__(self):
        super().__init__()
        self._constants = dict()
        self._lists = dict()
        self._fetch_constants()
        self._fetch_lists()

    def _fetch_constants(self):
        self._constants = self.get_lookup_data(DATA_MAPPING['location'],
                                                          DATA_MAPPING['constants'])

    def _fetch_lists(self):
        self._lists = self.get_lookup_data(DATA_MAPPING['location'],
                                                      DATA_MAPPING['lists'])

    def get_synth_fertilizer_nutrient_composition(self):
        return {
            'urea' :  self._constants['synth_fert_nutrient_urea_n'],
        }

    def get_climate_zone_emissions(self):
        n2o_n = self._lists['climate_n2o_n']
        nox_n = self._lists['climate_nox_n']
        climate_zones = self._lists['climate_zone']
        return pd.DataFrame((n2o_n,nox_n), index= climate_zones)

    def get_residue_est_from_dm_yield(self):
        names = self._lists['residue_crop_names']
        slope = self._lists['residue_slope']
        intercept = self._lists['residue_intercept']
        n_content_ag = self._lists['residue_n_content_ag']
        ratio_ag_to_bg = self._lists['residue_ratio_ag_to_bg']
        n_content_bg = self._lists['residue_n_content_bg']
        combustion = self._lists['residue_combustion']

        return pd.DataFrame(
            data=(slope, intercept, n_content_ag, n_content_bg, combustion, ratio_ag_to_bg),
            columns=('slope', 'intercept', 'n_content_ag', 'n_content_bg', 'combustion', 'ratio_ag_to_bg'),
            index=names)

    def get_n_loss_factors(self):
        return {
            'synthetic' : self._constants['loss_factor_synt_n'],
            'organic' : self._constants['loss_factor_org_n']
        }

    def get_p_loos_c2_factors_tillage(self):
        c2_factor = self._lists['p_loss_c2_till_factor']
        c2_tillage = self._lists['p_loss_c2_till']

        return pd.Series(c2_factor, index=c2_tillage)

    def get_res_burn_emissions(self):
        return {
            'n2o': self._constants['n2o_residue_burn_direct'],
            'nh3': self._constants['nh3_residue_burn_direct'],
            'nox': self._constants['nox_residue_burn_direct'],
            'ch4': self._constants['ch4_residue_burn_direct']
            }

    def get_co2_from_urea_and_lime(self):
        return {
            'urea': self._constants['co2_urea'],
            'lime': self._constants['co2_lime'],
            'dolomite': self._constants['co2_dolomite']
        }

    def get_n2o_from_residue(self):
        return self._constants['n2o_residue_direct']

    def get_regional_nox_emissions(self):
        factors = self._lists['nox_emiss_by_country']
        countries = self._lists['fao_countries_h']

        return pd.Series(factors, index= countries)

    def get_spatial_p_practices(self):
        p_index = self._lists['p_practice_by_location']
        p_index_locations = self._lists['p_practice_locations']

        return pd.Series(p_index, index= p_index_locations)

    def get_correction_for_practice_factor(self):
        factors = self._lists['correction_for_practice_factor']
        slope = self._lists['correction_for_practice_factor_slope']

        return pd.DataFrame((factors, slope), index=slope, columns=('Pcorr', 'Min'))

    def get_emissions_from_diesel(self):
        columns = ('production', 'combustion')

        ghg = (
            self._constants['ghg_disel_prod'],
            self._constants['ghg_disel_combustion']

        )
        acid = (
            self._constants['acid_disel_prod'],
            self._constants['acid_disel_combustion']

        )
        eutr = (
            self._constants['eutr_disel_prod'],
            self._constants['eutr_disel_combustion']
        )

        return pd.DataFrame(data=(ghg, acid, eutr), columns=columns, index=('ghg', 'acid','eutr'))

    def get_emissions_from_electricity_consumption_global(self):
        return {
            'ghg': self._constants['ghg_electricity'],
            'acid': self._constants['acid_elecrtricity'],
            'eutr': self._constants['eutr_electricity']}

    def get_emissions_from_machinery_and_infrastructure(self):
        columns = ('machinery','glass','plastic','rockwool','steel','aluminium','iron','concrete','wood')
        eutr =(
            self._constants['eutr_machinery'],
            self._constants['eutr_glass'],
            self._constants['eutr_plastic'],
            self._constants['eutr_rockwool'],
            self._constants['eutr_steel'],
            self._constants['eutr_aluminium'],
            self._constants['eutr_iron'],
            self._constants['eutr_concrete'],
            self._constants['eutr_wood']
        )
        ghg =(
            self._constants['ghg_machinery'],
            self._constants['ghg_glass'],
            self._constants['ghg_plastic'],
            self._constants['ghg_rockwool'],
            self._constants['ghg_steel'],
            self._constants['ghg_aluminium'],
            self._constants['ghg_iron'],
            self._constants['ghg_concrete'],
            self._constants['ghg_wood']
        )
        acid =(
            self._constants['acid_machinery'],
            self._constants['acid_glass'],
            self._constants['acid_plastic'],
            self._constants['acid_rockwool'],
            self._constants['acid_steel'],
            self._constants['acid_aluminium'],
            self._constants['acid_iron'],
            self._constants['acid_concrete'],
            self._constants['acid_wood']
        )

        return pd.DataFrame(data=(ghg, acid, eutr), columns=columns, index=('ghg','acid','eutr'))

    def get_emissions_from_electricity_consumption_by_country(self):
        columns =('country','gwp','so2','po4')
        countries = self._lists['electricity_emissions_countries']
        gwp = self._lists['gwp_from_elecrticity']
        so2 = self._lists['po4_from_elecrticity']
        po4 = self._lists['so2_from_electricity']

        return pd.DataFrame(data= (countries, gwp, so2, po4), columns= columns, index=countries)

    def get_nh3_tan_from_fert(self):
        return {
            'organic': pd.Series(self._lists['nh3_tan_from_org_fert']),
            'excreta': pd.Series(self._lists['nh3_emiss_from_excreta_tan'],
                                 index= self._lists['nh3_emiss_from_excreta_sources'])
        }

    def get_nh3_for_acidic_soil(self):
        table = self._lists['nh3_synth_acid_soil']
        temperatures = ('cool', 'temperate', 'warm')
        fertilizers = ('AP, DAP, MAP','AS','UAN Solu', 'AN, ACl, NP, NPK', 'CAN', 'AnhA, AquaA', 'AP, DAP, MAP')

        return pd.DataFrame(data=table, columns=fertilizers, index=temperatures)

    def get_nh3_for_alkaline_soil(self):
        table = self._lists['nh3_synth_alk_soil']
        temperatures = ('cool', 'temperate', 'warm')
        fertilizers = ('AP, DAP, MAP','AS','UAN Solu', 'AN, ACl, NP, NPK', 'CAN', 'AnhA, AquaA', 'AP, DAP, MAP')

        return pd.DataFrame(data=table, columns=fertilizers, index=temperatures)

    def get_p_loss_c2_factors_ctry(self):
        country = self._lists['fao_countries']
        c2_factor = self._lists['p_loss_c2_ctry_factor']

        return pd.Series(c2_factor, index=country)

    def get_p_loss_c1_factors_crop(self):
        crop = self._lists['p_loss_c1_crop']
        c1_factor = self._lists['p_loss_c1_crop_factor']

        return pd.Series(c1_factor, index=crop)

    def get_residue_burn_share(self):
        removed = self._lists['residue_burn_share']
        crop_name = self._lists['residue_removed_share_crops']
        country = self._lists['residue_removed_share_countries']

        return pd.DataFrame(data=removed,columns=country, index=crop_name)

    def get_residue_removed_share(self):
        removed = self._lists['residue_removed_share']
        crop_name = self._lists['residue_removed_share_crops']
        country = self._lists['residue_removed_share_countries']

        return pd.DataFrame(data=removed, columns=country, index=crop_name)

    def get_residue_burnt_share(self):
        removed = self._lists['residue_removed_share']
        crop_name = self._lists['residue_removed_share_crops']
        country = self._lists['residue_removed_share_countries']

        return pd.DataFrame(data=removed, columns=country, index=crop_name)

    def get_no3_leaching(self):
        return {
            'high': self._constants['c_leaching_no3_n_high'],
            'low': self._constants['c_leaching_no3_n_low'],
            'pasture': self._constants['c_leaching_no3_n_pasture'],
            'other': self._constants['c_leaching_no3_n_other'],
            'flooded_rice': self._constants['c_leaching_no3_n_flooded_rice']}

    def get_synth_fert_use(self):
        return {
            'global': self._constants['synth_fert_use_global']
        }

    def get_gwp(self):
        return {
            'n2o': self._constants['gwp_n2o'],
            'ch4': self._constants['gwp_ch4']
        }

    def get_atomic_weight_conversions(self):
        return{
            'n2on_n2o': self._constants['c_n2on_n2o'],
            'no3n_no3': self._constants['c_no3n_no3'],
            'nh3n_nh3': self._constants['c_nh3n_nh3'],
            'non_no': self._constants['c_non_no']
        }

    def get_default_n2o_emission_factors(self):
        pass

    def get_ipcc_crop_n2o_n(self):
        n2o_n = self._lists['ipcc_crops_n2o_n']
        crops = self._lists['ipcc_crops']

        return pd.Series(n2o_n, index=crops)