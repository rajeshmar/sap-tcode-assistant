import { useEffect, useState } from "react";
import {
  Clipboard,
  Loader2,
  Search,
  Sparkles,
  TerminalSquare,
  AlertCircle,
  CheckCircle2,
} from "lucide-react";
import { getModules, searchTcodes } from "./api/client";
import "./index.css";

const SAMPLE_QUERIES = [
  "check material",
  "create material",
  "create purchase order",
  "display sales order",
  "stock overview",
  "display invoice",
];

export default function App() {
  const [query, setQuery] = useState("");
  const [module, setModule] = useState("");
  const [modules, setModules] = useState([]);
  const [results, setResults] = useState([]);
  const [explanation, setExplanation] = useState("");
  const [loading, setLoading] = useState(false);
  const [modulesLoading, setModulesLoading] = useState(true);
  const [copiedCode, setCopiedCode] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    async function loadModules() {
      try {
        const moduleData = await getModules();
        setModules(moduleData);
      } catch (error) {
        setErrorMessage(
          "Unable to load SAP modules. Please confirm the backend is running on http://127.0.0.1:8000."
        );
        setModules([]);
      } finally {
        setModulesLoading(false);
      }
    }

    loadModules();
  }, []);

  async function runSearch(searchText = query) {
    const cleanedQuery = searchText.trim();

    if (!cleanedQuery) {
      setErrorMessage("Please enter a business need, for example: check material.");
      return;
    }

    setQuery(cleanedQuery);
    setLoading(true);
    setResults([]);
    setExplanation("");
    setErrorMessage("");

    try {
      const data = await searchTcodes({
        query: cleanedQuery,
        module,
        topK: 5,
      });

      setResults(data.results || []);
      setExplanation(data.explanation || "");

      if (!data.results || data.results.length === 0) {
        setErrorMessage(
          "No SAP T-Code matched your query. Try a more specific process name."
        );
      }
    } catch (error) {
      setErrorMessage(
        "Search failed. Please confirm the backend server is running on http://127.0.0.1:8000."
      );
      setExplanation("");
      setResults([]);
    } finally {
      setLoading(false);
    }
  }

  async function handleSearch(event) {
    event.preventDefault();
    await runSearch(query);
  }

  async function copyTcode(tcode) {
    try {
      await navigator.clipboard.writeText(tcode);
      setCopiedCode(tcode);

      setTimeout(() => {
        setCopiedCode("");
      }, 1200);
    } catch (error) {
      setErrorMessage("Unable to copy T-Code. Please copy it manually.");
    }
  }

  function selectModule(moduleCode) {
    setModule(moduleCode);
  }

  const bestResult = results[0];

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <section className="mx-auto max-w-7xl px-6 py-10">
        <header className="mb-10">
          <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-blue-400/20 bg-blue-400/10 px-4 py-2 text-sm text-blue-200">
            <Sparkles size={16} />
            SAP S/4HANA T-Code Assistant
          </div>

          <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr] lg:items-end">
            <div>
              <h1 className="text-4xl font-bold tracking-tight md:text-6xl">
                Find the right SAP T-Code instantly.
              </h1>

              <p className="mt-4 max-w-2xl text-lg leading-8 text-slate-400">
                Ask in simple language: check material, create purchase order,
                display sales order, stock overview, invoice display, and more.
              </p>
            </div>

            <div className="rounded-3xl border border-slate-800 bg-slate-900/70 p-5 shadow-2xl">
              <p className="text-sm uppercase tracking-widest text-slate-500">
                Current data source
              </p>
              <p className="mt-2 text-2xl font-semibold text-white">
                3,750 SAP transaction records
              </p>
              <p className="mt-2 text-sm text-slate-400">
                Powered by your extracted SAP S/4HANA T-Code knowledge base.
              </p>
            </div>
          </div>
        </header>

        <form
          onSubmit={handleSearch}
          className="rounded-[2rem] border border-slate-800 bg-slate-900 p-4 shadow-2xl"
        >
          <div className="flex flex-col gap-3 md:flex-row">
            <div className="relative flex-1">
              <Search
                className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500"
                size={22}
              />

              <input
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Example: I want to check material details"
                className="w-full rounded-2xl border border-slate-700 bg-slate-950 py-5 pl-14 pr-4 text-lg text-white outline-none transition placeholder:text-slate-600 focus:border-blue-400 focus:ring-4 focus:ring-blue-500/20"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="rounded-2xl bg-blue-500 px-8 py-5 font-semibold text-white transition hover:bg-blue-400 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <Loader2 className="animate-spin" size={18} />
                  Searching
                </span>
              ) : (
                "Find T-Code"
              )}
            </button>
          </div>

          <div className="mt-4 flex flex-wrap gap-2">
            <button
              type="button"
              onClick={() => selectModule("")}
              className={`rounded-full px-4 py-2 text-sm transition ${
                module === ""
                  ? "bg-blue-500 text-white"
                  : "bg-slate-800 text-slate-300 hover:bg-slate-700"
              }`}
            >
              All Modules
            </button>

            {modulesLoading ? (
              <span className="rounded-full bg-slate-800 px-4 py-2 text-sm text-slate-400">
                Loading modules...
              </span>
            ) : (
              modules.map((item) => (
                <button
                  key={item.code}
                  type="button"
                  onClick={() => selectModule(item.code)}
                  className={`rounded-full px-4 py-2 text-sm transition ${
                    module === item.code
                      ? "bg-blue-500 text-white"
                      : "bg-slate-800 text-slate-300 hover:bg-slate-700"
                  }`}
                  title={item.name}
                >
                  {item.code}
                </button>
              ))
            )}
          </div>

          <div className="mt-4 flex flex-wrap gap-2">
            {SAMPLE_QUERIES.map((sampleQuery) => (
              <button
                key={sampleQuery}
                type="button"
                onClick={() => runSearch(sampleQuery)}
                className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-400 transition hover:border-blue-400/50 hover:text-blue-200"
              >
                {sampleQuery}
              </button>
            ))}
          </div>
        </form>

        {errorMessage && (
          <section className="mt-6 flex items-start gap-3 rounded-2xl border border-red-400/20 bg-red-500/10 p-4 text-red-200">
            <AlertCircle className="mt-0.5 shrink-0" size={20} />
            <p>{errorMessage}</p>
          </section>
        )}

        {bestResult && (
          <section className="mt-8 rounded-[2rem] border border-blue-400/20 bg-gradient-to-br from-blue-500/20 to-slate-900 p-6 shadow-2xl">
            <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
              <div>
                <p className="text-sm uppercase tracking-widest text-blue-200">
                  Recommended transaction
                </p>

                <h2 className="mt-2 text-6xl font-black text-white">
                  {bestResult.tcode}
                </h2>

                <p className="mt-2 text-xl text-slate-200">
                  {bestResult.description}
                </p>

                <p className="mt-1 text-slate-400">
                  {bestResult.module_name} · Match score{" "}
                  {Math.round(bestResult.score)}%
                </p>
              </div>

              <button
                onClick={() => copyTcode(bestResult.tcode)}
                className="inline-flex items-center justify-center gap-2 rounded-2xl bg-white px-6 py-4 font-semibold text-slate-950 transition hover:bg-blue-100"
              >
                {copiedCode === bestResult.tcode ? (
                  <>
                    <CheckCircle2 size={18} />
                    Copied
                  </>
                ) : (
                  <>
                    <Clipboard size={18} />
                    Copy T-Code
                  </>
                )}
              </button>
            </div>
          </section>
        )}

        <section className="mt-8 grid gap-6 lg:grid-cols-5">
          <div className="lg:col-span-2">
            <div className="mb-4 flex items-center gap-2">
              <TerminalSquare className="text-blue-300" size={22} />
              <h2 className="text-xl font-semibold">Matching T-Codes</h2>
            </div>

            <div className="space-y-4">
              {loading && (
                <div className="rounded-3xl border border-slate-800 bg-slate-900 p-8 text-center text-slate-400">
                  <Loader2 className="mx-auto mb-3 animate-spin text-blue-300" />
                  Searching SAP transaction records...
                </div>
              )}

              {!loading &&
                results.map((result) => (
                  <article
                    key={`${result.tcode}-${result.description}-${result.module}`}
                    className="rounded-3xl border border-slate-800 bg-slate-900 p-5 transition hover:border-blue-400/40"
                  >
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <p className="text-sm text-slate-400">
                          {result.module_name}
                        </p>

                        <h3 className="mt-1 text-3xl font-bold text-blue-300">
                          {result.tcode}
                        </h3>
                      </div>

                      <button
                        onClick={() => copyTcode(result.tcode)}
                        className="rounded-xl bg-slate-800 p-3 text-slate-300 transition hover:bg-slate-700"
                        title="Copy T-Code"
                      >
                        <Clipboard size={18} />
                      </button>
                    </div>

                    <p className="mt-3 text-slate-200">
                      {result.description}
                    </p>

                    <div className="mt-4 h-2 rounded-full bg-slate-800">
                      <div
                        className="h-2 rounded-full bg-blue-500"
                        style={{ width: `${Math.round(result.score)}%` }}
                      />
                    </div>

                    <p className="mt-2 text-xs text-slate-500">
                      Match score: {Math.round(result.score)}%
                    </p>
                  </article>
                ))}

              {!loading && results.length === 0 && !errorMessage && (
                <div className="rounded-3xl border border-dashed border-slate-700 bg-slate-900/50 p-8 text-center text-slate-400">
                  Search for a business need to see recommended SAP T-Codes.
                </div>
              )}
            </div>
          </div>

          <div className="lg:col-span-3">
            <h2 className="mb-4 text-xl font-semibold">Usage Instructions</h2>

            <article className="min-h-[420px] whitespace-pre-wrap rounded-3xl border border-slate-800 bg-slate-900 p-6 text-base leading-8 text-slate-200 shadow-2xl">
              {loading
                ? "Finding the best SAP transaction code..."
                : explanation ||
                  "The assistant will explain the recommended T-Code and how to use it in SAP."}
            </article>
          </div>
        </section>
      </section>
    </main>
  );
}