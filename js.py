import js2py


x = js2py.eval_js("""
"use strict";
exports = {};
exports.__esModule = true;
exports.calculateBioAge = exports.getUserAge = exports.gendersMap = void 0;
exports.gendersMap = {
    male: { id: "male", name: "Male" },
    female: { id: "female", name: "Female" },
    diverse: { id: "diverse", name: "Diverse" },
    not_disclosed: { id: "not_disclosed", name: "Rather not say" }
};
// Get users Age in years based on their birthday date
var getUserAge = function (userBirthDate, decimals) {
    if (!userBirthDate) {
        return null;
    }
    ;
    var oneYearInMilliSeconds = 24 * 60 * 60 * 1000 * 365.25;
    var ageYearsDecimal = parseFloat(((new Date().getTime() - new Date(userBirthDate).getTime()) / oneYearInMilliSeconds).toFixed(decimals || 8));
    if (decimals) {
        return ageYearsDecimal;
    }
    ;
    return Math.floor(ageYearsDecimal);
};
exports.getUserAge = getUserAge;
;
;
var calculateBioAge = function (bioAgeCalcProps) {
    var _a, _b, _c, _d;
    var bio_age = bioAgeCalcProps.bio_age, measurements = bioAgeCalcProps.measurements, biomarker_values = bioAgeCalcProps.biomarker_values, userProfile = bioAgeCalcProps.userProfile, measurement_timestamp = bioAgeCalcProps.measurement_timestamp;
    // 1. Initialize variables and constants
    var msg = '';
    var biological_age = null;
    var mortality_score = null;
    var cronological_age = null; // Chron Age at time of test
    var date_of_birth = (_a = userProfile === null || userProfile === void 0 ? void 0 : userProfile.bio) === null || _a === void 0 ? void 0 : _a.date_of_birth;
    var gender = (_b = userProfile === null || userProfile === void 0 ? void 0 : userProfile.bio) === null || _b === void 0 ? void 0 : _b.gender;
    var height = (_c = userProfile === null || userProfile === void 0 ? void 0 : userProfile.bio) === null || _c === void 0 ? void 0 : _c.height_at_signup;
    var weight = (_d = userProfile === null || userProfile === void 0 ? void 0 : userProfile.bio) === null || _d === void 0 ? void 0 : _d.weight_at_signup;
    try {
        // Input values validation
        if (!measurement_timestamp) {
            var errorMsg = 'No Timestamp!';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        if (!date_of_birth) {
            var errorMsg = 'No Date of Birth!';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        if (!gender && (bio_age.id === 'pulmo_age')) {
            var errorMsg = 'No Gender!';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        if ((!height || height < 20 || height > 290) && (bio_age.id === 'pulmo_age')) {
            var errorMsg = 'No Height or out of range (20 - 290 cm)!';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        if ((!weight || weight < 1 || weight > 690) && (bio_age.id === 'in_body')) {
            var errorMsg = 'No Weight or out of Range (1 - 690 kg)!';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        if (new Date().getTime() < new Date(measurement_timestamp).getTime() || new Date().getTime() < new Date(date_of_birth).getTime()) {
            var errorMsg = 'Measurement or date of birth must be in the past';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        if (new Date(measurement_timestamp).getTime() < new Date(date_of_birth).getTime()) {
            var errorMsg = 'Measurement must be later than Birthday';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        var notAllValuesEntered_1 = false;
        Object.keys(biomarker_values || {}).map(function (bid) { return !biomarker_values[bid] && biomarker_values[bid] !== 0 ? notAllValuesEntered_1 = true : false; });
        if (notAllValuesEntered_1) {
            var errorMsg = 'Not all values entered';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        //// TODO: Validate against ranges
        //// TODO: Pick values and measurement timestamp from Health data points
        // Measurement timestamp (Time of blood draw)
        var timeSinceMeasurement = new Date().getTime() - new Date(measurement_timestamp).getTime();
        cronological_age = (0, exports.getUserAge)(new Date(date_of_birth).getTime() + timeSinceMeasurement, 2); // years, one decimal accuracy, age at blood draw
        // 2. Calculate Biological Age
        var calculatedBioAgeMarkers = void 0;
        switch (bio_age.id) {
            case 'pheno_age':
                calculatedBioAgeMarkers = calculatePhenoAge({ biomarker_values: biomarker_values, userProfile: userProfile, cronological_age: cronological_age });
                break;
            case 'pulmo_age':
                calculatedBioAgeMarkers = calculatePulmoAge({ biomarker_values: biomarker_values, userProfile: userProfile, cronological_age: cronological_age });
                break;
            default:
                break;
        }
        ;
        var biological_age_calculated = calculatedBioAgeMarkers === null || calculatedBioAgeMarkers === void 0 ? void 0 : calculatedBioAgeMarkers.biological_age_calculated;
        var mortality_score_calculated = calculatedBioAgeMarkers === null || calculatedBioAgeMarkers === void 0 ? void 0 : calculatedBioAgeMarkers.mortality_score_calculated;
        // 3. Validation and Report
        if (biological_age_calculated < 0 || biological_age_calculated > 200) {
            var errorMsg = 'Calculated Biological Age out of range 0-200';
            msg = msg + errorMsg + ', ';
            throw new Error(errorMsg);
        }
        ;
        // Add values
        biological_age = parseFloat(biological_age_calculated === null || biological_age_calculated === void 0 ? void 0 : biological_age_calculated.toFixed(2));
        mortality_score = parseFloat(mortality_score_calculated === null || mortality_score_calculated === void 0 ? void 0 : mortality_score_calculated.toFixed(4));
        msg = msg + 'No further errors in calculation.';
        // Report
        console.log("[".concat(bio_age.name, " Processor] Success calculating ").concat(bio_age.name, " (years): "), biological_age, 'Mortality Score (% 10 years): ', mortality_score, 'Chron. Age at draw (years): ', cronological_age, ' Messages: ', msg);
        return { biological_age: biological_age, mortality_score: mortality_score, cronological_age: cronological_age, msg: msg, status: 1 };
    }
    catch (error) {
        console.log("[".concat(bio_age.name, " Processor] Error calculating ").concat(bio_age.name, " (years): "), biological_age, 'Mortality Score (% 10 years): ', mortality_score, 'Chron. Age at draw (years): ', cronological_age, ' Messages: ', msg);
        return { biological_age: biological_age, mortality_score: mortality_score, cronological_age: cronological_age, msg: msg, status: -1 };
    }
};
exports.calculateBioAge = calculateBioAge;
;
;
// Based on https://pubmed.ncbi.nlm.nih.gov/7271065/
var calculatePulmoAge = function (bioAgeCalcFunctionProps) {
    var _a, _b;
    var biomarker_values = bioAgeCalcFunctionProps.biomarker_values, userProfile = bioAgeCalcFunctionProps.userProfile;
    var biological_age_calculated = null;
    var mortality_score_calculated = null;
    var gender = (_a = userProfile === null || userProfile === void 0 ? void 0 : userProfile.bio) === null || _a === void 0 ? void 0 : _a.gender;
    var height = (_b = userProfile === null || userProfile === void 0 ? void 0 : userProfile.bio) === null || _b === void 0 ? void 0 : _b.height_at_signup;
    // Biomarker values
    var FEV1 = biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.forced_expiratory_volume_1; // L/s
    if (gender === exports.gendersMap.male.id) {
        //Age(M) = (0.0414*height-2.19-FEV1)/0.0244
        biological_age_calculated = ((0.0414 * height) - 2.19 - FEV1) / 0.0244;
    }
    ;
    if (gender === exports.gendersMap.female.id) {
        //Age(F) = (0.0342*height-1.578-FEV1)/0.0255
        biological_age_calculated = ((0.0342 * height) - 1.578 - FEV1) / 0.0255;
    }
    ;
    return { biological_age_calculated: biological_age_calculated, mortality_score_calculated: mortality_score_calculated };
};
// This calculates the PhenoAge for a blood sample based on
// https://doi.org/10.18632/aging.101414
// and formulas from
// https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002760
var calculatePhenoAge = function (bioAgeCalcFunctionProps) {
    var biomarker_values = bioAgeCalcFunctionProps.biomarker_values, cronological_age = bioAgeCalcFunctionProps.cronological_age;
    var biological_age_calculated = null;
    var mortality_score_calculated = null;
    // Biomarker values
    var blood_albumin = (biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_albumin) * 10; // g/L      // <- g/dL
    var blood_creatinine = (biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_creatinine) * 88.42; // umol/L   // <- mg/dL
    var blood_glucose_serum = (biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_glucose_serum) * 0.0555; // mmol/L   // <- mg/dL
    var blood_c_reactive_protein_hs = (biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_c_reactive_protein_hs) * 0.1; // mg/dL    // <- mg/L
    var blood_lymphs = biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_lymphs; // %
    var blood_mean_corpuscular_volume = biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_mean_corpuscular_volume; // fL
    var blood_red_cell_distribution_width = biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_red_cell_distribution_width; // %
    var blood_alkaline_phosphatase = biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_alkaline_phosphatase; // U/L
    var blood_white_cell_count = biomarker_values === null || biomarker_values === void 0 ? void 0 : biomarker_values.blood_white_cell_count; // 1000 cells/uL
    // 2. Calculation
    // Phenotypic aging measures ans Gompertz coefficients
    var coeff_albumin = -0.0336; // negative
    var coeff_creatinine = 0.0095;
    var coeff_glucose_serum = 0.1953;
    var coeff_c_reactive_protein_hs = 0.0954;
    var coeff_lymphs = -0.0120; // negative
    var coeff_mean_corpuscular_volume = 0.0268;
    var coeff_red_cell_distribution_width = 0.3306;
    var coeff_alkaline_phosphatase = 0.0019; // 0.00188
    var coeff_white_cell_count = 0.0554;
    var coeff_cronological_age = 0.0804;
    var const_xb = -19.907; // negative
    // Calculate xb
    var xb = const_xb
        + coeff_albumin * blood_albumin
        + coeff_creatinine * blood_creatinine
        + coeff_glucose_serum * blood_glucose_serum
        + coeff_c_reactive_protein_hs * Math.log(blood_c_reactive_protein_hs)
        + coeff_lymphs * blood_lymphs
        + coeff_mean_corpuscular_volume * blood_mean_corpuscular_volume
        + coeff_red_cell_distribution_width * blood_red_cell_distribution_width
        + coeff_alkaline_phosphatase * blood_alkaline_phosphatase
        + coeff_white_cell_count * blood_white_cell_count
        + coeff_cronological_age * cronological_age;
    // Calculate Mortality Score
    var M = 1 - Math.exp((-1.51714 * Math.exp(xb)) / 0.0076927);
    // Calculate PhenoAge
    var pheno_age_calculated = 141.50 + (Math.log(-0.00553 * Math.log(1 - M)) / 0.09165);
    biological_age_calculated = pheno_age_calculated;
    mortality_score_calculated = M;
    return { biological_age_calculated: biological_age_calculated, mortality_score_calculated: mortality_score_calculated };
};
(0, exports.calculateBioAge)({
    bio_age: { id: 'pulmo_age', name: 'PulmoAge' },
    biomarker_values: { forced_expiratory_volume_1: 3 },
    userProfile: {
        header: {},
        bio: {
            date_of_birth: 545875200000,
            gender: 'male',
            weight_at_signup: 84,
            height_at_signup: 174
        }
    },
    measurement_timestamp: 1661252717369
});


""")
print(x)